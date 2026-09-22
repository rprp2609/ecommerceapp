const express = require('express');
const app = express();

app.get('/login', (req, res) => {
    const targetUrl = req.query.target;
    
    // DANGEROUS: Redirects to any external URL provided by the user
    res.redirect(targetUrl); 
});
