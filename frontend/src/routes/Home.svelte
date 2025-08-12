<script>
    import fastapi from "../lib/api"
    import { link } from 'svelte-spa-router'

    let question_list = []
    let size = 10
    let page = 0
    let total = 0
    // svelte에서 "$:" 는 변수앞에 붙으며 실시간으로 재 계산된다는 의미
    $: total_page = Math.ceil(total/size)

    // page에 따라 question_list를 변경
    function get_question_list(_page) {
        let params = {
            page: _page,
            size: size,
        }
        
        fastapi('get', '/api/question/list', params, (json) => {
            question_list = json.question_list
            page = _page
            total = json.total
        })
    }

    get_question_list(0)
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
    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center">
        <!--처음 페이지-->
        <li class="page-item {page <= 0 && 'disabled'}">
            <button class="page-link" on:click="{() => get_question_list(0)}">처음</button>
        </li>
        <!-- 이전페이지 -->
         <!--page가 0보다 작거나 같으면 비활성화-->
        <li class="page-item {page <= 0 && 'disabled'}">
            <button class="page-link" on:click="{() => get_question_list(page-1)}">이전</button>
        </li>
        <!-- ... 버튼 구현-->
        {#if page-5 > 0}
        <li class="page-item">
            <button class="page-link">...</button>
        </li>
        {/if}
        <!-- 페이지번호 -->
         <!-- 해당 페이지면 강조 -->
        {#each Array(total_page) as _, loop_page}
        
        <!--페이지 출력 제한-->
        {#if loop_page >= page-5 && loop_page <= page+5} 
        <li class="page-item {loop_page === page && 'active'}">
            <button on:click="{() => get_question_list(loop_page)}" class="page-link">{loop_page+1}</button>
        </li>
        {/if}
        {/each}
        <!-- ... 버튼 구현-->
        {#if page+5 < total_page-1}
        <li class="page-item">
            <button class="page-link">...</button>
        </li>
        {/if}
        <!-- 다음페이지 -->
        <li class="page-item {page >= total_page-1 && 'disabled'}">
            <button class="page-link" on:click="{() => get_question_list(page+1)}">다음</button>
        </li>
        <!--마지막 페이지-->
        <li class="page-item {page >= total_page-1 && 'disabled'}">
            <button class="page-link" on:click="{() => get_question_list(total_page-1)}">마지막</button>
        </li>
    </ul>
    <!-- 페이징처리 끝 -->
     <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a>
</div>