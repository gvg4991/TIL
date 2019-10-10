## Clock

- npm install

```
npm install moment --save
```



- vue

```vue
<template>
    <!-- clock -->
    <section id="app" class="section">
      <h3 class="title is-3 shadow" v-text="message"></h3>
      <p class="time shadow" v-text="currentTime"></p>
    </section>
</template>

<script>
var moment = require('moment')

export default {
  name: 'app',
  data() {
    return {
      message: 'Current Time:',
      currentTime: null,
        }
  }, 
    methods: {
  updateCurrentTime() {
      this.currentTime = moment().format('LTS');
    }
  },
   created() {
     this.currentTime = moment().format('LTS');
     setInterval(() => this.updateCurrentTime(), 1);
   }
}
</script>

<style>
 body, html {
  width: 100%;
  height: 100%;
} 

 body {
  background: -webkit-linear-gradient(LightSteelBlue, LightSalmon);
  background: -o-linear-gradient(LightSteelBlue, LightSalmon);
  background: -moz-linear-gradient(LightSteelBlue, LightSalmon);
  background: linear-gradient(LightSteelBlue, LightSalmon);
} 

 section.section {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 140px;
  background: transparent;
}

h3.is-3, p.time {
  color: white;
}

h3.is-3:not(:last-child) {
  margin: 0;
  padding: 0;
}

.time {
  font-size: 7em;
}

.shadow {
  text-shadow: 0 0 15px rgba(100, 100, 100, 0.35);
}

.pa-3{
  box-shadow: 0px 0px 10px #000;
  -moz-box-shadow: 0px 0px 10px #000;
  -webkit-box-shadow: 0px 0px 10px #000;
}
</style>
```

