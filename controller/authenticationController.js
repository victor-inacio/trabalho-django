const User = require('../models/User');

async function authenticate(req, res) {
    const user = await User.findOne({
        where: {
            email: req.body.email,
            password: req.body.password
        }
    });

    if (user != null) {
        req.session.authorized = true;
        req.session.user = user;
        res.redirect('/home_Page');
    } else {
        let error = true;
        res.render('login.html', {error});
    }
}

function verifyCookie(req, res, next) {
    if (req.session.authorized) {
        console.log("user authorized!");
        next();
    } else {
        console.log("user Not authorized");
        res.redirect('/');
    }
}

function logOut(req, res) {
    req.session.destroy();
    res.redirect('/');
}

module.exports = {
    authenticate,
    logOut
}