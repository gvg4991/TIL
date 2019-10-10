## Bookmark

- header.vue

```vue
<template>
    <v-btn
      small
      dark
      color="black"
      v-on:click="bookMarkAdd('포트폴리오','http://localhost:8080/Portfolio')"
    >
      <v-icon>bookmark_border</v-icon>Bookmark
    </v-btn>
</template>

<script>
  methods: {
    bookMarkAdd(title, url) {
      // IE
      if (document.all) {
        window.external.AddFavorite(url, title);
      }
      // Chrome
      else if (window.chrome) {
        alert("Ctrl+D키를 누르면 즐겨찾기 추가가 가능합니다.");
      }
      // Firefox
      else if (window.sidebar) {
        window.sidebar.addPanel(title, url, "");
      }
      // Opera
      else if (window.opera && window.print) {
        var elem = document.create.Element("a");
        elem.setAttribute("href", url);
        elem.setAttribute("title", title);
        elem.setAttribute("rel", "sidebar");
        elem.click();
      }
    }
  }
};
</script>
```

