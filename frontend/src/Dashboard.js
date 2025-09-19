import React, {useEffect, useState} from 'react';
import axios from 'axios';
export default function Dashboard(){


const [me, setMe] = useState(null);
async function register(){
  const u = prompt('username'); const e = prompt('email'); const p = prompt('password');
  if(!u||!e||!p) return; await axios.post('/api/auth/register/', {username:u,email:e,password:p}).catch(e=>alert('reg failed')); alert('registered');
}
async function login(){ const u = prompt('username'); const p = prompt('password'); if(!u||!p) return; const res = await axios.post('/api/auth/login/', {username:u,password:p}).catch(e=>{alert('login failed');}); if(res&&res.data) { alert('logged in'); fetchMe(); }}
async function logout(){ await axios.post('/api/auth/logout/').catch(()=>{}); setMe(null); alert('logged out'); }
async function fetchMe(){ const res = await axios.get('/api/me/donations/').catch(()=>null); if(res && Array.isArray(res.data)) setMe(true); }
useEffect(()=>{ fetch(); },[]);

  const [campaigns,setCampaigns]=useState([]);
  useEffect(()=>{ fetch(); },[]);
  async function fetch(){ const res = await axios.get('/api/campaigns/').catch(()=>({data:[]})); setCampaigns(res.data || []); }
  async function donate(c){
    const email = prompt('Your email for receipt (optional):');
    const amount = prompt('Donation amount in USD (e.g. 25.00):');
    if(!amount) return;
    const res = await axios.post('/api/paypal/create-order/', {campaign_id: c.id, email, amount}).catch(e=>{ alert('Failed to create order'); console.error(e); });
    if(res && res.data && res.data.approve_url){
      // open approval in new window; after approval PayPal will redirect to capture endpoint which returns JSON
      window.open(res.data.approve_url, '_blank');
      alert('Approval opened in a new tab. After approving, the capture endpoint will record donation.');
    }
  }
  async function subscribe(c){
    const email = prompt('Your email for subscription:');
    const amount = prompt('Monthly amount in USD (e.g. 5.00):');
    if(!amount || !email) return;
    const res = await axios.post('/api/paypal/create-subscription/', {campaign_id: c.id, email, amount}).catch(e=>{ alert('Failed to create subscription'); console.error(e); });
    if(res && res.data && res.data.approve_url){
      window.open(res.data.approve_url, '_blank');
      alert('Subscription approval opened in new tab.');
    }
  }
  async function payout(c){
    const amount = prompt('Payout amount in USD to campaign owner:');
    if(!amount) return;
    const res = await axios.post('/api/paypal/create-payout/', {campaign_id: c.id, amount}).catch(e=>{ alert('Payout failed'); console.error(e); });
    if(res && res.data) alert('Payout created: ' + JSON.stringify(res.data));
  }
  return (<div>
<button onClick={register}>Register</button> <button onClick={login}>Login</button> <button onClick={logout}>Logout</button> <button onClick={viewMyDonations}>My Donations</button> <button onClick={viewMySubs}>My Subscriptions</button> <button onClick={refundDon}>Refund</button> <button onClick={cancelSub}>Cancel Sub</button>

    <h2>Campaigns</h2>
    <table border='1' cellPadding='8'><thead><tr><th>Title</th><th>Goal</th><th>Owner Email</th><th>Actions</th></tr></thead><tbody>{campaigns.map(c=>(<tr key={c.id}><td>{c.title}</td><td>${(c.goal_cents/100).toFixed(2)}</td><td>{c.owner_email}</td><td><button onClick={()=>donate(c)}>Donate</button> <button onClick={()=>subscribe(c)}>Subscribe</button> <button onClick={()=>payout(c)}>Payout</button></td></tr>))}</tbody></table>
    <p>Notes: Donations open PayPal approval windows. After approving, PayPal redirects to our capture endpoint which records the donation. Subscriptions also require approval.</p>
  </div>);
}
