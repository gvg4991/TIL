## Header & SideBar

- header.vue

```vue
<template>
  <!-- <v-toolbar fixed app> -->
  <v-app style="position:absolute;">
    <div class="toolbar">
      <v-toolbar fixed app class="fixed-header" color="#557984">
          
        <!--sidebar icon & hidden -->
        <v-toolbar-side-icon
          @click.stop="sideNav = !sideNav"
          class="hidden-md-and-up"
          style=" color:#F7EFF1;"
        >
          <v-icon class="menu-icon">menu</v-icon>
        </v-toolbar-side-icon>

        <!-- homepage icon -->
        <router-link to="/" style="font-size: 35px; color:#F7EFF1;">
          <i class="far fa-smile"></i>
		</router-link>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-sm-and-down headerlogo">
          <v-btn flat to="/Post"  style="font-size: 16px; color:#F7EFF1;">Post</v-btn>
          <v-btn flat to="/Portfolio"  style="font-size: 16px; color:#F7EFF1;">Portfolio</v-btn>
        </v-toolbar-items>
    </v-toolbar>
   </div>
          
          <!--sidebar-->
    <v-navigation-drawer temporary style="position:fixed" v-model="sideNav">
      <v-list>
        <v-list-tile v-for="item in menuItems" :key="item.title" :to="item.link">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>{{ item.title }}</v-list-tile-content>

          <!-- <v-list-tile-content to="/login" class="nav-btn" v-if="!$store.state.loginCheck">Login</v-list-tile-content> -->
          <!-- 로그인 로그아웃 firebase상태에 따른표시 -->
          <!-- <v-list-tile-content v-on:click="logOut" class="nav-btn" v-if="$store.state.loginCheck">Logout</v-list-tile-content>
          <v-list-tile-content to="/hi" class="nav-btn" v-if="$store.state.loginCheck">HI</v-list-tile-content>-->
        </v-list-tile>
    </v-list>
  </v-navigation-drawer>
 </v-app>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
      sideNav: false,
      menuItems: [
        { icon: "portrait", title: "Portfolio", link: "/portfolio" },
        { icon: "photo_filter", title: "Post", link: "/post" }
      ]
    };
  }
</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Open+Sans:800);
    
a,
a:visited {
  color: black;
  text-decoration: none;
  font-size: 20px;
}
.headerlogo {
  font-family: "Russo One", sans-serif;
}
.fixed-header {
  position: fixed;
  top: 0px;
  z-index: 1;
}
</style>
```



- app.vue

```vue
<template>
  <v-app style="background:#E5E6DA;">
      <Header class="notranslate"></Header>
      <router-view />
      <Footer class="notranslate"></Footer>
  </v-app>
</template>

<script>
import store from "./store";
import Header from "./components/Header";
import Footer from "./components/Footer";

export default { 
  name: "App",
  components: {
    Header,
    Footer
  },
  store,
  data() {
    return {
      //
    };
  }

var agent = navigator.userAgent.toLowerCase();
var name = navigator.appName;
```

