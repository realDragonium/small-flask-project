FROM node:14-alpine

WORKDIR /usr/src/app

COPY rollup.config.js ./
COPY package*.json ./

RUN yarn

COPY ./src ./src
COPY ./public ./public

RUN yarn run build

CMD [ "yarn", "run", "start", "--host", "0.0.0.0" ]