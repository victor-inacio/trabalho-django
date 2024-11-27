const Sequelize = require('sequelize');
const database = require('../db');

const Task = database.define('task', {
    id: {
        type: Sequelize.UUID,
        defaultValue: Sequelize.UUIDV4,
        allowNull: false,
        primaryKey: true
    },
    user_id: {
        type: Sequelize.UUID,
        allowNull: false
    },
    title: {
        type: Sequelize.STRING,
        allowNull: false
    },
    description: {
        type: Sequelize.STRING,
        allowNull: false
    },
    priority: {
        type: Sequelize.INTEGER,
        allowNull: false
    },
    deadline: {
        type: Sequelize.DATE,
        allowNull: false
    },
    done: {
        type: Sequelize.BOOLEAN
    },
    parent_id: {
        type: Sequelize.UUID,
        allowNull: true
    }
});

Task.hasMany(Task, {
    foreignKey: 'parent_id',
    as: 'subtasks'
});

Task.belongsTo(Task, {
    foreignKey: 'parent_id',
    as: 'parentTask'
});

module.exports = Task;