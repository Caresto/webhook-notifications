# webhook-notifications
Simple Flask Webhook receiver


To install you need to have Docker in your machine

# Building Image
Replace Dockerfile URL with the desired URL

```docker build -t <reeplace value>-notifier .```

# To run image
```docker run -d --name <>-notifier-container -p <desired port>:80 <reeplace value>-notifier```
