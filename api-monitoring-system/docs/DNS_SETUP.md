# DNS Configuration Guide

## Required Records
1. **A Record**:
   - Name: @ (or yourdomain.com)
   - Value: [Your server IP]
   - TTL: 3600

2. **CNAME Record (www)**:
   - Name: www
   - Value: yourdomain.com
   - TTL: 3600

## Verification
After setting up:
```bash
dig yourdomain.com
dig www.yourdomain.com
```
Should return your server IP