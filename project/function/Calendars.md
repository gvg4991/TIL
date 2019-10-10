## Calendars

calendars.vue

```vue
<template>
<!-- 포스트리스트 compo에서 쓰이기위한 틀 만들기 -->
<v-layout wrap>
    <v-flex sm12>
      <v-sheet height="64">
        <v-toolbar flat color="white">
          <v-btn outlined class="mr-2" outline color="black" @click="setToday">
            today
          </v-btn>
          <div>{{ today }}<br>{{ currentTime }}</div>
          
          <v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer>
          <v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer>
          <v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer>
          <v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer>
          <v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer>
  <!-- <v-layout wrap>
    <v-flex
      sm12
      lg3
      class="mb-4 controls"
    > -->
      <v-btn
        fab
        outlined
        small
        color="white"
        @click="prev"
      >
        <v-icon dark>
          keyboard_arrow_left
        </v-icon>
      </v-btn>


      <h2>{{ month }}월</h2>

      <v-btn
        fab
        outlined
        small
        color="white"
        @click="next"
      >
        <v-icon dark>
          keyboard_arrow_right
        </v-icon>
      </v-btn>
          
      <!-- <v-select
        v-model="type"
        :items="typeOptions"
        label="Type"
      ></v-select> -->

      <!-- <v-checkbox
        v-model="dark"
        label="Dark"
      ></v-checkbox> -->

        </v-toolbar>
      </v-sheet>

      <!-- <v-checkbox
        v-model="dark"
        label="Dark"
      ></v-checkbox>
      <v-checkbox
        v-model="shortIntervals"
        label="Short intervals"
      ></v-checkbox>
      <v-checkbox
        v-model="shortMonths"
        label="Short months"
      ></v-checkbox>
      <v-checkbox
        v-model="shortWeekdays"
        label="Short weekdays"
      ></v-checkbox>
      <v-select
        v-model="color"
        :items="colorOptions"
        label="Color"
      ></v-select>
      <v-menu
        ref="startMenu"
        v-model="startMenu"
        :close-on-content-click="false"
        :nudge-right="40"
        :return-value.sync="start"
        transition="scale-transition"
        min-width="290px"
        offset-y
        full-width
      >
        <template v-slot:activator="{ on }">
          <v-text-field
            v-model="start"
            label="Start Date"
            prepend-icon="event"
            readonly
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="start"
          no-title
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn
            text
            color="primary"
            @click="startMenu = false"
          >
            Cancel
          </v-btn>
          <v-btn
            text
            color="primary"
            @click="$refs.startMenu.save(start)"
          >
            OK
          </v-btn>
        </v-date-picker>
      </v-menu>
      <v-menu
        v-if="hasEnd"
        ref="endMenu"
        v-model="endMenu"
        :close-on-content-click="false"
        :nudge-right="40"
        :return-value.sync="end"
        transition="scale-transition"
        min-width="290px"
        offset-y
        full-width
      >
        <template v-slot:activator="{ on }">
          <v-text-field
            v-model="end"
            label="End Date"
            prepend-icon="event"
            readonly
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="end"
          no-title
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn
            text
            color="primary"
            @click="endMenu = false"
          >
            Cancel
          </v-btn>
          <v-btn
            text
            color="primary"
            @click="$refs.endMenu.save(end)"
          >
            OK
          </v-btn>
        </v-date-picker>
      </v-menu>
      <v-menu
        ref="nowMenu"
        v-model="nowMenu"
        :close-on-content-click="false"
        :nudge-right="40"
        :return-value.sync="now"
        transition="scale-transition"
        min-width="290px"
        offset-y
        full-width
      >
        <template v-slot:activator="{ on }">
          <v-text-field
            v-model="now"
            label="Today"
            prepend-icon="event"
            readonly
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="now"
          no-title
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn
            text
            color="primary"
            @click="nowMenu = false"
          >
            Cancel
          </v-btn>
          <v-btn
            text
            color="primary"
            @click="$refs.nowMenu.save(now)"
          >
            OK
          </v-btn>
        </v-date-picker>
      </v-menu> -->
      <!-- <v-select
        v-model="weekdays"
        :items="weekdaysOptions"
        label="Weekdays"
      ></v-select>
      <v-text-field
        v-if="type === 'custom-weekly'"
        v-model="minWeeks"
        label="Minimum Weeks"
        type="number"
      ></v-text-field>
      <v-select
        v-if="hasIntervals"
        v-model="intervals"
        :items="intervalsOptions"
        label="Intervals"
      ></v-select>
      <v-select
        v-if="type === 'custom-daily'"
        v-model="maxDays"
        :items="maxDaysOptions"
        label="# of Days"
      ></v-select>
      <v-select
        v-if="hasIntervals"
        v-model="styleInterval"
        :items="styleIntervalOptions"
        label="Styling"
      ></v-select> -->
    </v-flex>

    <v-flex sm12>
      <v-sheet height="570">
        <v-calendar
          ref="calendar"
          v-model="focus"
          :type="type"
          :start="start"
          :end="end"
          :min-weeks="minWeeks"
          :max-days="maxDays"
          :now="now"
          :dark="dark"
          :weekdays="weekdays"
          :first-interval="intervals.first"
          :interval-minutes="intervals.minutes"
          :interval-count="intervals.count"
          :interval-height="intervals.height"
          :interval-style="intervalStyle"
          :show-interval-label="showIntervalLabel"
          :short-intervals="shortIntervals"
          :short-months="shortMonths"
          :short-weekdays="shortWeekdays"
          :color="color"
        >
        
        <!-- 캘린더 내용부분 -->
          <template v-slot:day="{ date }">
            <div 
                style="overflow:auto; height:70px;">
            <template v-if="date == today">
              <!-- <v-btn to="/PostWriter"><i class="far fa-calendar-plus fa-lg"></i></v-btn> -->
              <v-btn small fab dark color="indigo" to="/PostWriter">
                <v-icon>edit</v-icon>
              </v-btn>
            </template>
            <template v-for="event in eventsMap[date]">
              <v-menu
                :key="event.id"
                full-width
                offset-x
              >
                <template v-slot:activator="{ on }">
                  <div
                    v-if="!event.time"
                    v-ripple
                    class="my-event"
                    v-on="on"
                    v-html="event.title"
                  ></div>
                </template>
                <v-card class='notranslate'
                  color="grey lighten-4"
                  min-width="350px"
                  flat
                >
                  <v-toolbar
                    color="primary"
                    dark
                  >
                    <v-btn icon>
                      <v-icon>edit</v-icon>
                    </v-btn>
                    <v-toolbar-title v-html="event.title"></v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-btn icon>
                      <v-icon>more_vert</v-icon>
                    </v-btn>
                  </v-toolbar>
                  <v-card-title primary-title>
                    <span v-html="event.body"></span>
                  </v-card-title>
                  <v-card-actions>
                    <v-btn
                      flat
                      color="secondary"
                    >
                      Cancel
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-menu>
            </template>
            </div>
          </template>
        </v-calendar>
      </v-sheet>
    </v-flex>
  </v-layout>
</template>


<script>
import PostWriter from '../views/PostWriterPage'
	
var moment = require('moment')

  const weekdaysDefault = [0, 1, 2, 3, 4, 5, 6]

  const intervalsDefault = {
    first: 0,
    minutes: 60,
    count: 24,
    height: 40,
  }

  const stylings = {
    default (interval) {
      return undefined
    },
    workday (interval) {
      const inactive = interval.weekday === 0 ||
        interval.weekday === 6 ||
        interval.hour < 9 ||
        interval.hour >= 17
      const startOfHour = interval.minute === 0
      const dark = this.dark
      const mid = dark ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.1)'

      return {
        backgroundColor: inactive ? (dark ? 'rgba(0,0,0,0.4)' : 'rgba(0,0,0,0.05)') : undefined,
        borderTop: startOfHour ? undefined : '1px dashed ' + mid,
      }
    },
    past (interval) {
      return {
        backgroundColor: interval.past ? (this.dark ? 'rgba(0,0,0,0.4)' : 'rgba(0,0,0,0.05)') : undefined,
      }
    },
  }

  export default {
    data: () => ({
      today: moment().format('YYYY-MM-DD'),
      month: Number(moment().format('M')),
      focus: moment().format(),
      message: 'Current Time:',
      currentTime: null,
      dark: false,
      startMenu: false,
      start: moment().format(),
      endMenu: false,
      end: '2019-12-27',
      nowMenu: false,
      minWeeks: 1,
      now: null,
      type: 'month',
      typeOptions: [
        { text: 'Day', value: 'day' },
        { text: 'Week', value: 'week' },
        { text: 'Month', value: 'month' },
      ],
      weekdays: weekdaysDefault,
      weekdaysOptions: [
        { text: 'Sunday - Saturday', value: weekdaysDefault },
        { text: 'Mon, Wed, Fri', value: [1, 3, 5] },
        { text: 'Mon - Fri', value: [1, 2, 3, 4, 5] },
        { text: 'Mon - Sun', value: [1, 2, 3, 4, 5, 6, 0] },
      ],
      intervals: intervalsDefault,
      intervalsOptions: [
        { text: 'Default', value: intervalsDefault },
        { text: 'Workday', value: { first: 16, minutes: 30, count: 20, height: 40 } },
      ],
      maxDays: 7,
      maxDaysOptions: [
        { text: '7 days', value: 7 },
        { text: '5 days', value: 5 },
        { text: '4 days', value: 4 },
        { text: '3 days', value: 3 },
      ],
      styleInterval: 'default',
      styleIntervalOptions: [
        { text: 'Default', value: 'default' },
        { text: 'Workday', value: 'workday' },
        { text: 'Past', value: 'past' },
      ],
      color: 'deep-purple',
      colorOptions: [
        { text: 'Primary', value: 'primary' },
        { text: 'Secondary', value: 'secondary' },
        { text: 'Accent', value: 'accent' },
        { text: 'Red', value: 'red' },
        { text: 'Pink', value: 'pink' },
        { text: 'Purple', value: 'purple' },
        { text: 'Deep Purple', value: 'deep-purple' },
        { text: 'Indigo', value: 'indigo' },
        { text: 'Blue', value: 'blue' },
        { text: 'Light Blue', value: 'light-blue' },
        { text: 'Cyan', value: 'cyan' },
        { text: 'Teal', value: 'teal' },
        { text: 'Green', value: 'green' },
        { text: 'Light Green', value: 'light-green' },
        { text: 'Lime', value: 'lime' },
        { text: 'Yellow', value: 'yellow' },
        { text: 'Amber', value: 'amber' },
        { text: 'Orange', value: 'orange' },
        { text: 'Deep Orange', value: 'deep-orange' },
        { text: 'Brown', value: 'brown' },
        { text: 'Blue Gray', value: 'blue-gray' },
        { text: 'Gray', value: 'gray' },
        { text: 'Black', value: 'black' },
      ],
      shortIntervals: true,
      shortMonths: false,
      shortWeekdays: true,
    }),
    props: {
      events: {type: Array}
    },
    components: {
      PostWriter
    },
    computed: {
      eventsMap () {
        const map = {}
        this.events.forEach(e => (map[e.date] = map[e.date] || []).push(e))
        return map
      },
      intervalStyle () {
        return stylings[this.styleInterval].bind(this)
      },
      hasIntervals () {
        return this.type in {
          week: 1, day: 1, '4day': 1, 'custom-daily': 1,
        }
      },
      hasEnd () {
        return this.type in {
          'custom-weekly': 1, 'custom-daily': 1,
        }
      },
    },
    methods: {
      // open (event) {
      //   alert(event.title)
      // }
      viewDay ({ date }) {
        this.focus = moment().format()
        this.type = 'day'
      },
      getEventColor (event) {
        return event.color
      },
      showIntervalLabel (interval) {
        return interval.minute === 0
      },
      // 현재 날짜시간 정보를 focus에 넣기 (data에 focus를 정의해 줬기때문에 이용 가능)
      setToday () {
        this.focus = moment().format()
        this.month = Number(moment().format('M'))
      },
      updateCurrentTime() {
      this.currentTime = moment().format('LTS');
      },
      prev() {
        this.$refs.calendar.prev()
        this.month = this.month - 1
        if (this.month === 0)
        this.month = 12
      },
      next() {
        this.$refs.calendar.next()
        this.month = this.month + 1
        if (this.month === 13)
        this.month = 1
      }
    },
    created() {
     this.currentTime = moment().format('LTS');
     setInterval(() => this.updateCurrentTime(), 1);
   }
  }
</script>



<style lang="stylus" scoped>
  .my-event {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    border-radius: 2px;
    background-color: #663399;
    color: #ffffff;
    border: 1px solid #663399;
    width: 100%;
    font-size: 12px;
    padding: 3px;
    cursor: pointer;
    margin-bottom: 1px;
  }
</style>
```





postlist.vue

```vue
<template>
  <v-layout row wrap mw-700>
    <!-- <v-flex
      xs12
      sm6
      v-for="i in posts.length > limits ? limits : posts.length"
      :class="'xs' + 12 / column"
      px-3
    >
      <Post :date="posts[i - 1].created_at" :title="posts[i - 1].title" :body="posts[i - 1].body"></Post>
      <v-divider></v-divider>
    </v-flex> -->
    
    <!-- <v-flex
    class = 'notranslate'
      xs12
      v-for="i in posts.length > limits ? limits : posts.length"
      px-3
    >
      <Calendars :date="posts[i - 1].created_at" :title="posts[i - 1].title" :body="posts[i - 1].body"></Calendars>
    </v-flex> -->
    <v-flex xs12 px-3>
      <Calendars :events="posts"></Calendars>
    </v-flex>

    <!-- <v-flex xs12 text-xs-center round my-5 v-if="loadMore">
      <v-btn color="info" dark v-on:click="loadMorePosts">
        <v-icon size="25" class="mr-2">fa-plus</v-icon>더 보기
      </v-btn>
    </v-flex> -->
  </v-layout>
</template>
<script>
import Post from "@/components/Post";
import Calendars from "@/components/Calendars";
import FirebaseService from "@/services/FirebaseService";

export default {
  name: "PostList",
  props: {
    column: { type: Number, default: 1 },
    limits: { type: Number, default: 4 },
    loadMore: { type: Boolean, default: false }
  },
  data() {
    return {
      posts: []
    };
  },
  components: {
    Post,
    Calendars
  },
  mounted() {
    this.getPosts();
  },
  methods: {
    async getPosts() {
      this.posts = await FirebaseService.getPosts();
    },
    loadMorePosts() {}
  }
};
</script>
<style>
.mw-700 {
  max-width: 700px;
  margin: auto;
}
</style>

```





post.vue

```vue
<template>
  <v-layout py-4 h-100>
    <v-flex row>
      <div class="caption">{{formatedDate}}</div>
      <h2 class="color-333 headline font-weight-light" v-line-clamp="1">{{title}}</h2>
      <p class="mb-1 color-666 font-weight-light subheading" v-line-clamp:20="3">{{body}}</p>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
	name: 'Post',
	props: {
		date: {type: Date},
		title: {type: String},
		body: {type: String}
	},
  computed: {
		formatedDate() {
			return `${this.date.getFullYear()}년 ${this.date.getMonth()}월 ${this.date.getDate()}일`
    }
  }
}
</script>
<style>
  .color-666 {
    color: #666;
  }
  .color-333 {
    color: #333;
  }
  .h-100 {
    height: 100%;
  }
</style>


```







FirebaService.js

```js
import firebase from "firebase/app";
import "firebase/firestore";
import "firebase/auth";
import "firebase/messaging";
import store from "../store";

const POSTS = "posts";
const PORTFOLIOS = "portfolios";
const COMMENTS = "comments";
const USER = "user";
const USERINFO = "userInfo";

// Setup Firebase
const config = {
  apiKey: "AIzaSyABEKC5ObMwCwiyoW_JYytS5n9fyEkL_gM",
  authDomain: "webmobile-pjt02-f41b9.firebaseapp.com",
  databaseURL: "https://webmobile-pjt02-f41b9.firebaseio.com",
  projectId: "webmobile-pjt02-f41b9",
  storageBucket: "webmobile-pjt02-f41b9.appspot.com",
  messagingSenderId: "586747368733",
  appId: "1:586747368733:web:80489c4413d0e5a8"
};

firebase.initializeApp(config);
const firestore = firebase.firestore();

firebase
  .firestore()
  .enablePersistence()
  .catch(function(err) {
    if (err.code == "failed-precondition") {
      // Multiple tabs open, persistence can only be enabled
      // in one tab at a a time.
      // ...
    } else if (err.code == "unimplemented") {
      // The current browser does not support all of the
      // features required to enable persistence
      // ...
    }
  });

var database = firebase.database();

//푸쉬알림
const messaging = firebase.messaging();
messaging.usePublicVapidKey(
  "BAT35xZR5_hEPJYwxml8KMMDQeL6X4mbrxeqNeP9UqWAovkAtNNLoLXd5hF4P_zyr2phL4qFZXGqLoCBln6qtcU"
);

messaging
  .requestPermission()
  .then(function() {
    console.log("메세징 권한 획득");
    return messaging.getToken();
  })
  .then(function(token) {
    console.log("fcm token : ", token);
  })
  .catch(function(e) {
    console.log("메세징 권한 획득 중 에러", e);
  });

messaging.onMessage(function(payload) {
  console.log('onmessage:', payload);
  var options = {
      body: payload.notification.body,
      icon: payload.notification.icon
      // click_action : "http://localhost:8080"
  }
  var notification = new Notification(payload.notification.title, options);

});


export default {
  messageSender(to, title, body, img) {
    var key = 'AAAAiJzeVR0:APA91bH-8xO5UPwwvHRU4BnSUrqYFC0T3ZlMsXEHLHXLxwqWi2Xb3XEUn1Fo8FBF1xUUipV-_JbA9KShFwyJ_6Oyr1zWkdR3EtEuEFuMtn1x5GHbumiU8MCIj_6YhqvS81yGgPxxUDfD';
    var notification = {
        'title': title,
        'body': store.state.displayName+'님이 '+body,
        'icon': img
    };
    fetch('https://fcm.googleapis.com/fcm/send', {
        'method': 'POST',
        'headers': {
            'Authorization': 'key=' + key,
            'Content-Type': 'application/json'
        },
        'body': JSON.stringify({
            'notification': notification,
            'to': to
        })
    }).then(function(response) {
        console.log(response);
    }).catch(function(error) {
        console.error(error);
    })
},

  getPosts() {
    const postsCollection = firestore.collection(POSTS);
    return postsCollection
      .orderBy("date", "desc")
      .get()
      .then(docSnapshots => {
        return docSnapshots.docs.map(doc => {
          let data = doc.data();
          data.id = doc.id;
          return data;
        });
      });
  },
  postPost(title, body) {
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!

    if(dd<10) {dd='0'+dd} 

    if(mm<10) {mm='0'+mm} 

    today = today.getFullYear()+'-'+mm+'-'+dd;

    return firestore.collection(POSTS).add({
      title,
      body,
      date: today,
      created_at: firebase.firestore.FieldValue.serverTimestamp()
    });
  },

  setPortfolio(title, body, img, id, name) {
    return firestore
      .collection(PORTFOLIOS)
      .doc(id.toString())
      .set({
        title,
        body,
        img,
        id,
        name,
        created_at: firebase.firestore.FieldValue.serverTimestamp()
      });
  },

  deletePortfolios(id) {
    const postsCollection = firestore.collection(PORTFOLIOS);
    postsCollection.doc(id).delete();
  },
  // =======
  // messaging.onMessage(function (payload) {
  //   console.log('Message received. ', payload);
  //   // ...
  // });

  // FirebaseChat.prototype.setLogin = function (user) { //user 파라미터 추
  //   //...생략
  //   this.saveFCMToken();
  // }

  // /** * FCM Token 저장 */
  // FirebaseChat.prototype.saveFCMToken = function () {

  // }

  //로그인 후에 fcm 정보를 검색하여 저장
  // const cbGetToekn = function(token){
  //   console.log('setLogin fcmId get : ', token);
  //   var userUid = this.auth.currentUser.uid;
  //   var fcmIdRef= this.database.ref('FcmId/' +userUid);
  //   fcmIdRef.set(token);
  // }

  // firebase.messaging().getToken()
  // .then(cbGetToekn.bind(this))
  // .catch(function(e){
  //   console.log('fcmId 확인 중 에러 : ', e);
  // })

  // getPortfoliosbyId(id) {
  //   const postsCollection = firestore.collection(PORTFOLIOS).doc(id);
  //   return postsCollection.get().then(doc => {
  //     let data = doc.data();
  //     data.created_at = new Date(data.created_at.toDate());
  //     return data;
  //   });
  // },

  // postPortfolio(title, body, img, id) {
  //   return firestore
  //     .collection(PORTFOLIOS)
  //     .doc(id.toString())
  //     .set({
  //       title,
  //       body,
  //       img,
  //       id,
  //       created_at: firebase.firestore.FieldValue.serverTimestamp()
  //     });
  // },

  // getComments() {
  //   const commentsCollection = firestore.collection(COMMENTS);
  //   return commentsCollection
  //     .orderBy("created_at", "desc")
  //     .get()
  //     .then(docSnapshots => {
  //       return docSnapshots.docs.map(doc => {
  //         let data = doc.data();
  //         data.created_at = new Date(data.created_at.toDate());
  //         return data;
  //   },

  getPortfolios() {
    const postsCollection = firestore.collection(PORTFOLIOS);
    return postsCollection
      .orderBy("created_at", "desc")
      .get()
      .then(docSnapshots => {
        return docSnapshots.docs.map(doc => {
          let data = doc.data();
          data.id = doc.id;
          data.created_at = new Date(data.created_at.toDate());
          return data;
        });
      });
  },

  getPortfoliosbyId(id) {
    const postsCollection = firestore.collection(PORTFOLIOS).doc(id);
    return postsCollection.get().then(doc => {
      let data = doc.data();
      data.created_at = new Date(data.created_at.toDate());
      return data;
    });
  },

  postPortfolio(title, body, img, name) {
    return firestore.collection(PORTFOLIOS).add({
      title,
      body,
      img,
      name,
      created_at: firebase.firestore.FieldValue.serverTimestamp()
    });
  },

  getComments(id) {
    const postsCollection = firestore
      .collection(PORTFOLIOS)
      .doc(id)
      .collection(COMMENTS);
    return postsCollection
      .orderBy("created_at", "asc")
      .get()
      .then(docSnapshots => {
        return docSnapshots.docs.map(doc => {
          let data = doc.data();
          data.id = doc.id;
          return data;
        });
      });
  },

  postComment(id, name, comment) {
    return firestore
      .collection(PORTFOLIOS)
      .doc(id)
      .collection(COMMENTS)
      .add({
        name,
        comment,
        created_at: firebase.firestore.FieldValue.serverTimestamp()
      });
  },

  deleteComment(id, i) {
    const postsCollection = firestore
      .collection(PORTFOLIOS)
      .doc(id)
      .collection(COMMENTS);
    postsCollection.doc(i).delete();
  },
  setComment(id, i, name, comment, ca) {
    return firestore
      .collection(PORTFOLIOS)
      .doc(id)
      .collection(COMMENTS)
      .doc(i)
      .set({
        comment,
        name,
        created_at: ca
      });
  },

  loginWithGoogle() {
    let provider = new firebase.auth.GoogleAuthProvider();
    return firebase
      .auth()
      .signInWithPopup(provider)
      .then(function(result) {
        // let accessToken = result.credential.accessToken;
        // let user = result.user;
        return result;
      })
      .catch(function(error) {
        console.error("[Google Login Error]", error);
      });
  },
  loginWithFacebook() {
    let provider = new firebase.auth.FacebookAuthProvider();

    return firebase
      .auth()
      .signInWithPopup(provider)
      .then(result => {
        // let accessToken = result.credential.accessToken;
        // let user = result.user;
        console.log(result.user);
        // alert("페이스북 로그인 성공");
        return result;
      })
      .catch(err => {
        alert("에러" + err.message);
      });
  },
  // },
  addLog(id, msg) {
    //firebase에 로그인/로그아웃 log report
    return firestore
      .collection(USER)
      .doc(id)
      .collection("history")
      .add({
        created_at: firebase.firestore.FieldValue.serverTimestamp(),
        msg: msg
      })
  },

  tokenRefresh() {
    return this.getFCMToken().then(token => {
      firestore
        .collection(USERINFO)
        .doc(store.state.user.uid)
        .update({
          token: token
        })
    });
  },

  getFCMToken() {
    return Notification.requestPermission()
      .then(function(permission) {
        if (permission === "granted") {
          return messaging.getToken();
        } else {
          return null;
        }
      })
      .then(result => {
        return result;
      });
  },

  getUserTokens(){
    return firestore
    .collection(USERINFO)
    .get()
    .then(docSnapshots => {
      return docSnapshots.docs.map(doc => {
        return doc.data().token;
      });
    });
  },

  getAdminTokens(){
    return firestore
    .collection(USERINFO)
    .get()
    .then(docSnapshots => {
      return docSnapshots.docs.map(doc => {
        if(doc.data().auth=="admin")
          return doc.data().token;
        else
          return null;
      });
    });
  },



  // getUserInfoList() {
  //   //database에서 회원정보 모두 읽어오기
  //   var users = [];
  //   firestore
  //     .collection("userInfo")
  //     .get()
  //     .then(querySnapshot => {
  //       querySnapshot.forEach(doc => {
  //         let data = doc.data();
  //         data.created_at = new Date(data.created_at.toDate());

  //         users.push(data);
  //       });
  //     });
  //   return users;
  // },

  // loginWithFacebook() {
  //   let provider = new firebase.auth.FacebookAuthProvider();

  //   return firebase
  //     .auth()
  //     .signInWithPopup(provider)
  //     .then(result => {
  //       // let accessToken = result.credential.accessToken;
  //       // let user = result.user;
  //       console.log(result.user);
  //       // alert("페이스북 로그인 성공");
  //       return result;
  //     })
  //     .catch(err => {
  //       alert("에러" + err.message);
  //     });
  // },
  // },
  // addLog(id, msg) {
  //   //firebase에 로그인/로그아웃 log report
  //   return firestore
  //     .collection(USER)
  //     .doc(id)
  //     .collection("history")
  //     .add({
  //       created_at: firebase.firestore.FieldValue.serverTimestamp(),
  //       msg: msg
  //     })
  //     .then(function() {
  //       console.log("update log");
  //     });
  // },
  async registerUser(user) {
    var docRef = firestore.collection(USERINFO).doc(user.uid);

    await docRef.get().then(result => {
      if (result.data()) {
        //result.data()가 있으면 true, 없으면 false (=null 값)이라면, 아무것도 안함
        console.log("정보가 저장되어있는 살람입니다");
      } else {
        //DB에 유저를 저장함 ( 한번만 작용하게됨 )
        this.getFCMToken().then(token => {
          const docData = {
            displayName: user.displayName,
            email: user.email,
            created_at: firebase.firestore.FieldValue.serverTimestamp(),
            auth: "visitor",
            token: token
          };
          console.log(docData);
          return docRef.set(docData).then(function() {
            console.log("register user");
          });
        });
      }
    });
  },

  getUserInfo(uid) {
    //database에서 사용자 정보 읽기 (로그인시 세션으로 데이터 활용)
    var userRef = firestore.collection(USERINFO).doc(uid);
    return userRef.get().then(doc => {
      let userdata = doc.data();
      return userdata;
    });
  },

  getUserInfoList() {
    //database에서 회원정보 모두 읽어오기
    var users = [];
    firestore
      .collection("userInfo")
      .get()
      .then(querySnapshot => {
        querySnapshot.forEach(doc => {
          var data = doc.data();
          data.uid = doc.id;

          if (data.uid != firebase.auth().currentUser.uid) {
            //로그인한 admin 계정 외의 정보만 users리스트에 넣음

            data.created_at = new Date(data.created_at.toDate())
              .toString()
              .slice(4, 16);

            users.push(data);
          }
        });
      });
    return users;
  },
  async getUsersCnt() {
    //회원수 카운트
    var usersCnt = [4];
    var totalCnt = 0;
    var adminCnt = 0;
    var memberCnt = 0;
    var visitorCnt = 0;

    await firestore
      .collection("userInfo")
      .get()
      .then(
        await function(querySnapshot) {
          querySnapshot.forEach(doc => {
            var data = doc.data();

            totalCnt += 1;

            if (data.auth == "admin") {
              adminCnt += 1;
            } else if (data.auth == "member") {
              memberCnt += 1;
            } else {
              visitorCnt += 1;
            }
          });
        }
      );

    usersCnt[0] = totalCnt;
    usersCnt[1] = adminCnt;
    usersCnt[2] = memberCnt;
    usersCnt[3] = visitorCnt;

    // console.log(usersCnt);

    return usersCnt;
  },
  async getPortfoliosCnt() {
    //총 포트폴리오수
    var totalCnt = 0;

    await firestore
      .collection("portfolios")
      .get()
      .then(
        await function(querySnapshot) {
          querySnapshot.forEach(doc => {
            // console.log(data);
            totalCnt += 1;
          });
        }
      );
    return totalCnt;
  }
};

```

