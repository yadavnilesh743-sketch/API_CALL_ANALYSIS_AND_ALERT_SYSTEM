#!/bin/bash

# Install Vercel CLI if needed
if ! command -v vercel &> /dev/null
then
    npm install -g vercel
fi

# Deploy frontend
cd frontend
vercel --prod --confirm