/*global Vue, todoStorage */

Vue.config.productionTip = false;
var api_enpoint = 'http://127.0.0.1:5000/todos';

(function (exports) {

	'use strict';

	var filters = {
		all: function (todos) {
			return todos;
		},
		active: function (todos) {
			return todos.filter(function (todo) {
				return !todo.completed;
			});
		},
		completed: function (todos) {
			return todos.filter(function (todo) {
				return todo.completed;
			});
		}
	};

	exports.app = new Vue({

		// the root element that will be compiled
		el: '.todoapp',

		// app initial state
		data: {
			todos: [],
			newTodo: '',
			editedTodo: null,
			visibility: 'all'
		},

		// computed properties
		// http://vuejs.org/guide/computed.html
		computed: {
			filteredTodos: function () {
				return filters[this.visibility](this.todos);
			},
			remaining: function () {
				return filters.active(this.todos).length;
			},
			allDone: {
				get: function () {
					return this.remaining === 0;
				},
				set: function (value) {
					var app_todos = this;
					this.todos.forEach(function (todo) {
						todo.completed = value;
						app_todos.updateTodo(todo);
					});
				}
			}
		},
		created: function () {
			var app = this;
		    axios.get(api_enpoint).then(function (response) {
				app.todos = response.data;
			});
  		},
		// methods that implement data logic.
		// note there's no DOM manipulation here at all.
		methods: {

			pluralize: function (word, count) {
				return word + (count === 1 ? '' : 's');
			},

			addTodo: function () {
				var app_todo = this;
				var value = this.newTodo && this.newTodo.trim();
				if (!value) {
					return;
				}
				var todo_data = {id: 0, title: value, completed: false};
				axios.put(api_enpoint, todo_data).then(function(response) {
					todo_data['id'] = response.data.id;
					app_todo.todos.push(todo_data);
					app_todo.newTodo = '';
				});
			},

			removeTodo: function (todo) {
				axios.delete(api_enpoint, {data: this.convertToJson(todo)});
				var index = this.todos.indexOf(todo);
				this.todos.splice(index, 1);
			},

			editTodo: function (todo) {
				this.beforeEditCache = todo.title;
				this.editedTodo = todo;
			},

			doneEdit: function (todo) {
				if (!this.editedTodo) {
					return;
				}
				this.editedTodo = null;
				todo.title = todo.title.trim();
				if (!todo.title) {
					this.removeTodo(todo);
				} else {
					this.updateTodo(todo);
				}
			},

			cancelEdit: function (todo) {
				this.editedTodo = null;
				todo.title = this.beforeEditCache;
			},

			removeCompleted: function () {
				this.todos = filters.active(this.todos);
			},

			updateTodo: function (todo) {
				axios.post(api_enpoint, this.convertToJson(todo));
			},

			convertToJson: function (todo) {
				return {id: todo.id, title: todo.title, completed: todo.completed};
			}
		},

		// a custom directive to wait for the DOM to be updated
		// before focusing on the input field.
		// http://vuejs.org/guide/custom-directive.html
		directives: {
			'todo-focus': function (el, binding) {
				if (binding.value) {
					el.focus();
				}
			}
		}
	});

})(window);
