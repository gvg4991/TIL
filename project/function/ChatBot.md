## ChatBot

- 참조 링크

```
https://codevkr.tistory.com/74
https://calyfactory.github.io/api.ai-chatbot/
https://closer.ai/
https://pusher.com/chatkit
https://danbee.ai/platform/#/nlu/nlu_intentdetail/cfe71d8c-81c1-4386-bd1e-2b4f70ce3b5b
```



- danbee open API

```
https://doc.danbee.ai/channel_frogu.html
```



- index.html

```html
<body>
	<!-- 챗봍 -->
	<!-- key값: be67d7bd-9b4c-4e51-a347-5ceea194ff55 -->
    <div class="notranslate">
    <div id="frogue-container" class="position-right-bottom" data-chatbot="be67d7bd-9b4c-4e51-a347-5ceea194ff55" data-user="사용자ID" data-init-key="be67d7bd-9b4c-4e51-a347-5ceea194ff55"></div>
    </div>  
      <script>
      (function(d, s, id){
          var js, fjs = d.getElementsByTagName(s)[0];
          if (d.getElementById(id)) {return;}
          js = d.createElement(s); js.id = id;
          js.src = "https:\/\/danbee.ai/js/plugins/frogue-embed/frogue-embed.min.js";
          fjs.parentNode.insertBefore(js, fjs);
      }(document, 'script', 'frogue-embed'));
      </script>
</body>
```



