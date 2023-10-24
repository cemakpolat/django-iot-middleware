# Use an official Node runtime as a parent image
FROM node:16 as build

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install app dependencies
RUN npm install
# Install Angular CLI
RUN npm install -g @angular/cli
# Copy the rest of the application code into the container
COPY . .

# Build the Angular app for production
RUN ng build 

# Use a lightweight Nginx image to serve the Angular app
FROM nginx:alpine

# Copy the built Angular app from the build stage to the Nginx web server directory
COPY --from=build /app/dist/app1 /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# Start Nginx web server
CMD ["nginx", "-g", "daemon off;"]
