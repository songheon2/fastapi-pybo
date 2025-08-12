<!--URL 규칙-->
<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"
  import QuestionCreate from "./routes/QuestionCreate.svelte"
  import Navigation from "./components/Navigation.svelte"

  // '/' 주소는 Hom.svelte
  const routes = {
    '/': Home,
    '/detail/:question_id': Detail,
    '/question-create': QuestionCreate,
  }
</script>

<!--네비게이션 컴포넌트를 모든 페이지에 표시-->
<Navigation />
<Router {routes}/>