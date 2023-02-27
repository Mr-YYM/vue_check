<template>
    <div class="ports">
      <h1>Port Information</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>IP Address</th>
            <th>Port Number</th>
            <th>Is Open</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="port in ports" :key="port.id">
            <td>{{ port.id }}</td>
            <td>{{ port.ip_address }}</td>
            <td>{{ port.port_number }}</td>
            <td>
                <span v-if="port.is_open" class="badge bg-success">✔</span>
                <span v-else class="badge bg-danger">✘</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Ports',
    data() {
      return {
        ports: [],
      };
    },
    async created() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/ports/ports/');
        this.ports = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  };
  </script>
  
  <style>
  table {
    border-collapse: collapse;
    width: 100%;
  }
  
  th, td {
    text-align: left;
    padding: 8px;
  }
  
  th {
    background-color: #4CAF50;
    color: white;
  }
  .text-danger {
    color: red;
  }
  .text-success {
    color: green;
  }
  </style>
  