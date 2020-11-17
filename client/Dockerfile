FROM node:12.18-alpine
ENV NODE_ENV=production
ENV BROWSER=none
ENV PORT=80
ENV REACT_APP_API_URL=https://api-catpic.azurewebsites.net
WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
RUN npm install --production --silent
COPY . .
EXPOSE 80
CMD ["npm", "start"]
