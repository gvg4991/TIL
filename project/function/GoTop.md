## GoTop

- vue

```vue
 <v-btn fixed fab bottom right style="cursor:pointer; display:none; bottom:80px;" v-on:click="goTop()" id="MOVE_TOP_BTN">
   <v-icon class="notranslate">keyboard_arrow_up</v-icon>
 </v-btn>

<script>
export default { 
  	methods: {
    goTop(){
      window.scrollTo({
                top: 0,
                left: 0,
                behavior: "smooth"
            });
    }
  }
};
    
window.addEventListener('scroll', function() {
  var el = document.querySelector('#MOVE_TOP_BTN');

  if(window.scrollY <= 50) {
    el.style.display = "none";
  }else {
    el.style.display = "block";
  }
});
</script>
```



