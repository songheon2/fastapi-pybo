<script>
    import fastapi from "../lib/api"
    import { link } from 'svelte-spa-router'

    let question_list = []

    function get_question_list() {
        //직접 정의한 api.js lib 사용
        fastapi('get', '/api/question/list', {}, (json) => {
            question_list = json
        })
    }

    get_question_list()
</script>

<!--div, table, 하위 속성들에 bootstrap에서 제공하는 class로 지정-->
<div class="container my-3">
    <table class="table">
        <thead>
        <tr class="table-dark">
            <th>번호</th>
            <th>제목</th>
            <th>작성일시</th>
        </tr>
        </thead>
        <tbody>
        {#each question_list as question, i}
        <tr>
            <td>{i+1}</td>
            <td>
                 <!--use:link  = serverURL다음에 '/#'이 선행되게 함
                해당 형식으로 서버에 요청하면 # 뒤로는 서버가 무시
                => serverURL/로 처리
                => /#뒷 부분은 브라우저가 js로 처리
                => 서버는 동일한 페이지로 인식
                href="" = serverURL다음에 붙일 요청할 경로-->
                <a use:link href="/detail/{question.id}">{question.subject}</a>
            </td>
            <td>{question.create_date}</td>
        </tr>
        {/each}
        </tbody>
    </table>
     <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a>
</div>