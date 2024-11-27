const db = require('./db');

const express = require('express');
const mustacheExpress = require('mustache-express');
const session = require('express-session');
const app = express();

const PORT = 8080;

app.engine('html', mustacheExpress());
app.set('view engine', 'html');
app.set('views', __dirname + `/views`);
app.use(express.urlencoded({extended: true}));

app.use(session({
    secret: 'secret-token',
    name: 'sessionId',  
    resave: false,
    saveUninitialized: false
}))

app.use('/', require('./routers/toDoRouter'));
app.use('/', require('./routers/authenticationRouter'));
app.use('/', require('./routers/userRouter'));

db.sync();

app.listen(PORT, ()=>{
    console.log(`App running at PORT: ${PORT}`);
});