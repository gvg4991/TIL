## Translator

- 참조 링크

```
https://www.w3schools.com/howto/tryit.asp?filename=tryhow_google_translate
```



- index.html

```html
<head>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
</head>

<body>
    <noscript>
      <strong>We're sorry but ssafy doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>
    <div id="app"></div>
    <!-- built files will be auto injected -->
    <script src="http://code.jquery.com/jquery-1.10.2.js"></script>
    <script type="text/javascript">
    // 1.basic
      // function googleTranslateElementInit() {
      //   new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element');
      // }
    // 2.simple select button
      // function googleTranslateElementInit() {
      //   new google.translate.TranslateElement({pageLanguage: 'ko',includedLanguages: 'ko,en',
      //       layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
      //       autoDisplay: false}, 'google_translate_element');
      // }
    // 3.list button
    function googleTranslateElementInit() {
      new google.translate.TranslateElement({pageLanguage:'ko', layout: google.translate.TranslateElement.FloatPosition.TOP_LEFT, autoDisplay:false}, 'google_translate_element');
    }
    function triggerHtmlEvent(element, eventName) {
      var event;
      if (document.createEvent) {
        event = document.createEvent('HTMLEvents');
        event.initEvent(eventName, true, true);
        element.dispatchEvent(event);
      } else {
        event = document.createEventObject();
        event.eventType = eventName;
        element.fireEvent('on' + event.eventType, event);
      }
    }

    jQuery('.lang-select').click(function() {
      var theLang = jQuery(this).attr('data-lang');
      jQuery('.goog-te-combo').val(theLang);

      //alert(jQuery(this).attr('href'));
      window.location = jQuery(this).attr('href');
      location.reload();

    });
    </script>
      
    <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>  
</body>

<style>
    /* 구글 번역 위에 팝업창 뜨지 않게 하기 위해서 넣은 CSS*/
    .goog-te-banner-frame.skiptranslate {
    display: none !important;
    }
</style>
```



- header.vue

```vue
<!-- 번역 -->
        <div class="text-xs-center mb-1">
          <v-menu offset-y>
            <template v-slot:activator="{ on }">
              <button
                type="button"
                class="v-toolbar__side-icon v-btn v-btn--icon theme--white"
                aria-label="Menu"
                v-on="on"
              >
                <div class="v-btn__content">
                  <i class="fas fa-language fa-3x"></i>
                </div>
              </button>
            </template>
            <v-list>
              <v-list-tile>
                <a
                  href="#googtrans(en|en)"
                  class="lang-en lang-select"
                  data-lang="en"
                  @click="reload"
                >
                  <img src="img/en.png" alt="USA" height="20px" width="30px" /> ENG
                </a>
              </v-list-tile>
              <v-list-tile>
                <a
                  href="#googtrans(en|ko)"
                  class="lang-ko lang-select"
                  data-lang="ko"
                  @click="reload"
                >
                  <img src="img/ko.png" alt="KOREA" height="20px" width="30px" /> KOR
                </a>
              </v-list-tile>
            </v-list>
          </v-menu>
        </div>

<script>
    methods: {
        reload() {
          setTimeout(function() {
            window.location.reload();
          }, 300);
        },
</script>
```



- 번역 제외

```vue
<div class="notranslate">...</div>
```

