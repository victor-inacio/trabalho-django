const express = require('express');
const router = express.Router();

const authenticationController = require('../controller/authenticationController');

router.post('/authenticate', authenticationController.authenticate);
router.get('/logOut', authenticationController.logOut);

module.exports = router;