const Task = require ('../models/Task');
const Op = require('sequelize');

function showIndex(req, res) {
    res.render('Login.html');
}

function showSignIn(req, res) {
    res.render('sign_in.html');
}

function showHome(req, res) {
    Task.findAll({
        where: {
            user_id: req.session.user.id,
            // deadline: {
            //     [Op.gt]: new Date(),
            // }
        }
    }).then((tasks)=>{
        console.log(tasks);
        res.render('home_Page', {tasks});
    }).catch((task_fetch_failure)=>{
        res.render('home_Page', {task_fetch_failure});
    })
}

function showTaskCreation(req, res) {
    res.render('task_register.html');
}

function createTask(req, res) {
    let task = {
        user_id: req.session.user.id,
        title: req.body.title,
        description: req.body.description,
        priority: req.body.priority,
        deadline: req.body.deadline,
        subtasks: req.body.subtasks
    }

    console.log(task);

    Task.create(task).then(()=>{
        res.redirect('/home_Page');
    }).catch((error)=>{
        console.log(error);
        let task_creation_error = true;
        res.redirect('/home_page', {task_creation_error});
    });
}

async function deleteTask(req, res) {
    try {
        const { id } = req.body;
        await Task.destroy({ where: { id, user_id: req.session.user.id } });
        res.redirect('/home_Page');
    } catch (error) {
        console.error("Error deleting task: ", error);
        res.status(500).send("Error deleting task");
    }
}

async function editTask(req, res) {
    try {
        const { id, title, description, priority, deadline, done } = req.body;
        await Task.update(
            { title, description, priority, deadline, done },
            { where: { id, user_id: req.session.user.id } }
        );
        res.redirect('/home_Page');
    } catch (error) {
        console.error("Error updating task: ", error);
        res.status(500).send("Error updating task");
    }
}

module.exports = {
    showIndex,
    showSignIn,
    showHome,
    showTaskCreation,
    createTask,
    deleteTask,
    editTask,
}