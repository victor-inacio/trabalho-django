const express = require('express');
const router = express.Router();

const toDoController = require('../controller/toDoController');
const authenticationController = require('../controller/authenticationController');

router.get('/', toDoController.showIndex);
router.get('/home_Page', toDoController.showHome);
router.get('/task_register', toDoController.showTaskCreation);
router.post('/create_task', toDoController.createTask);
router.post('/delete_task', toDoController.deleteTask);
router.post('/edit_task', toDoController.editTask);
router.get('/sign_in', toDoController.showSignIn);

module.exports = router;