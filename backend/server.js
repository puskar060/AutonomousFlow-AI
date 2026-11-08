const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = new Server(server, { cors: { origin: "*" } });

io.on('connection', (socket) => {
  console.log(`Client connected: ${socket.id}`);
  socket.on('agent_state_update', (data) => {
    io.emit('live_workflow_update', data);
  });
});

server.listen(4000, () => {
  console.log('OmniWorker Real-Time Socket Server running on port 4000');
});
