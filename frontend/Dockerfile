FROM node:18-alpine
WORKDIR /app
COPY package.json .
RUN npm install --no-progress --no-audit --silent
COPY . .
CMD ["npm", "start"]
