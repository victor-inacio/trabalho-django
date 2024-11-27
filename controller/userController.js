const User = require('../models/User');

function signUser(req, res) {
    let user = {
        name: req.body.name,
        email: req.body.email,
        password: req.body.password,
    }

    console.log(user);

    User.create(user).then(()=>{
        let success = true;
        res.render('login.html', {success});
    }).catch((err)=>{
        console.log(err);
        let sign_error = true;
        res.render('login.html', {sign_error});
    });
}

function listUsers(req, res) {
    User.findAll().then((users)=>{
        res.json(users);
    }).catch((err)=>{
        res.json(err);
    });
}

module.exports = {
    signUser,
    listUsers
}