<script>
    import fastapi from "../lib/api"
<<<<<<< HEAD

    export let params = {}
    let question_id = params.question_id
    console.log('question_id:'+ question_id)    
    let question = {}
=======
    import Error from "../components/Error.svelte"

    export let params = {}
    let question_id = params.question_id
    // debug 
    //console.log('question_id:'+ question_id)    
    let question = {answers:[]}
    // 답변 내용
    let content = ""
    let error = {detail:[]}

>>>>>>> c418497 (2-7답변등록까지 커밋)

    function get_question() {
        fastapi("get", "/api/question/detail/" + question_id, {}, (json) => {
            question = json
        })
    }

    get_question()
<<<<<<< HEAD
=======

    // 답변 등록 API 호출 함수 (답변 등록 버튼 클릭시 실행)
    function post_answer(event) {
        // 버튼의 default 행동 방지
        event.preventDefault()
        let url = "/api/answer/create/" + question_id
        let params = {
            content: content
        }
        fastapi('post', url, params, 
            (json) => {
                content = ''
                // 이전에 있던 오류 메시지 초기화
                error = {detail:[]}
                get_question()
            },
            // failute_callback 함수
            (err_json) => {
                error = err_json
            }
        )
    }
>>>>>>> c418497 (2-7답변등록까지 커밋)
</script>

<h1>{question.subject}</h1>
<div>
    {question.content}
<<<<<<< HEAD
</div>
=======
</div>
<ul>
    {#each question.answers as answer}
        <li>{answer.content}</li>
    {/each}
</ul>
<!--에러 출력-->
<Error error={error} />
<form method="post">
    <!--답변 내용 입력
    textarea에 값을 추가하거나 변경할 때마다 content의 값도 자동으로 변경할 수 있게
    content와 연결-->
    <textarea rows="15" bind:value={content}></textarea>
    <!--답변 등록 버튼-->
    <input type="submit" value="답변등록" onclick="{post_answer}">
</form>
>>>>>>> c418497 (2-7답변등록까지 커밋)
