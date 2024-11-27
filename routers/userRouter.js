const express = require('express');
const router = express.Router();

const userController = require('../controller/userController');

router.post('/sign_user', userController.signUser);
router.post('/api/users', userController.listUsers);

module.exports = router;