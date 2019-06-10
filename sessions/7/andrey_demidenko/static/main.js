$(document).ready(function(){

    var socket = io();
    socket.on('connect', function() {
        socket.emit('user_connected');
    });
    socket.on('refresh_users', function(users){
        refreshUsers(users)
    });

    function refreshUsers(users)
    {
        if (!$.isEmptyObject(users)) {
            $('#list-users').html('');
            $.each(users, function (index, user) {
                var html = '<li class="clearfix">\n' +
                        '<img class="avatar" src="https://petition.dailytrust.com/storage/petition_avatar.png" alt="avatar" />' +
                        '<div class="about">' +
                        '<div class="name">' + user.user_name + '</div>' +
                        '<div class="status">' +
                        '<i class="fa fa-circle online"></i> online' +
                        '</div>' +
                        '</div>' +
                        '</li>';
                $('#list-users').append(html);
            });
        }
    }

    socket.on('message', function(message){
        var $chatHistory = $('.chat-history');
        var userId = $chatHistory.data('user-id');
        messageHtml = '<li class="clearfix">' +
            '<div class="message-data ' + (userId === message.user_id ? '' : 'align-right') + '">' +
            (userId === message.user_id ?
            '<i class="fa fa-circle online"></i> <span class="message-data-name" >' + message.username + '</span><span class="message-data-time" >' + message.time + '</span>'
                :  '<span class="message-data-time" >' + message.time + '</span> <span class="message-data-name" >' + message.username + '</span> <i class="fa fa-circle me"></i>') +
            '</div>' +
            '<div class="message ' + (userId === message.user_id ? 'my-message' : 'other-message float-right') + '">' + message.message + '</div>' +
            '</li>';
        $('.chat-history ul').append(messageHtml);
        $chatHistory.scrollTop($chatHistory[0].scrollHeight);
    });

    $('#send-button').on('click', function() {
        socket.emit('message', $('#message-to-send').val());
        $('#message-to-send').val('');
    });

    $('#logout-button').on('click', function() {
        if (confirm('Do you want to logout ?') ) {
            $.post( "/logout", function() {
                socket.emit('user_logout');
                location.href = '/login';
            });
        }
    });

});
