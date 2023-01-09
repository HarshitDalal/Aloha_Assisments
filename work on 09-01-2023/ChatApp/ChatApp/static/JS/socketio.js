const socket = io.connect("http://127.0.0.1:5000/");
    socket.on('connect', () => {
        socket.emit('join_room', {
            username: "{{ username }}",
            room: "{{ room }}"
        });
    });
    let message_input = document.getElementById('message_input');

    document.getElementById('message_input_form').onsubmit = (e) => {
        e.preventDefault();
        let message = message_input.value.trim();
        if (message.length) {
            socket.emit('send_message', {
                username: "{{ username }}",
                room: "{{ room }}",
                message: message
            })
        }
        message_input.value = '';
        message_input.focus();
    };

    socket.on('join_room_announcement', (data) => {
        if (data.username !== "{{ username }}") {
            const newNode = document.createElement('p');
            newNode.innerHTML = `<b>${data.username}</b> has joined the room`;
            document.getElementById('messages').appendChild(newNode);
        }
    });

    socket.on('receive_message', (data) => {
        const newNode = document.createElement('div');
        newNode.innerHTML = `<b>${data.username}:&nbsp;</b> ${data.message}`;
        document.getElementById('messages').appendChild(newNode);
    });