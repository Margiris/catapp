FROM node:12.18-alpine
ENV NODE_ENV=production
ENV BROWSER=none
ENV REACT_APP_API_URL=http://127.0.0.1:5000
WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
RUN npm install --production --silent
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
