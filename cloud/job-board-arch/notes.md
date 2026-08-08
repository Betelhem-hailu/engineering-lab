# Notes

## Why do I need a load balancer?

A load balancer distributes incoming requests across multiple backend instances. This prevents one instance from becoming overloaded and allows the application to continue serving traffic if an instance fails.
Auto Scaling can work with it to add or remove instances based on demand.

## Why shouldn't my database be publicly accessible?

The database should normally be private because users don't need direct access to it. Only trusted backend services should be able to communicate with it, reducing the attack surface and allowing database access to be controlled through network rules.

## What should go into S3 instead of PostgreSQL?

s3 is object storage which will store files like images, texts and videos using a key.

## Why might I need Redis?

Redis isn't only a cache. It can also be used for sessions, rate limiting, queues, distributed locks, and other use cases.

## What happens if one backend instance dies?

If one backend instance fails, the load balancer can stop sending traffic to that unhealthy instance and route requests to the healthy instances. Auto Scaling can then replace the failed instance.
                    User
                      │
                      ▼
                 Route 53
                      │
                      ▼
               Load Balancer
                      │
             ┌────────┴────────┐
             ▼                 ▼
        Backend API       Backend API
             │                 │
             └────────┬────────┘
                      │
             ┌────────┴────────┐
             ▼                 ▼
          PostgreSQL           S3
             │
             ▼
           Redis