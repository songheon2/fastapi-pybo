const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation
    let content_type = 'application/json'
    //params 객체를 JSON문자열로 반환
    let body = JSON.stringify(params)

    let _url = import.meta.env.VITE_SERVER_URL+url
    if(method === 'get') {
        _url += "?" + new URLSearchParams(params)
    }

    let options = {
        method: method,
        headers: {
            "Content-Type": content_type
        }
    }

    if (method !== 'get') {
        options['body'] = body
    }

    fetch(_url, options)
        .then(response => {
<<<<<<< HEAD
=======
            // 답변 등록 API는 응답 결과가 없기 때문에 예외 추가
            // success_callback을 실행할 수 있도록
            if(response.status === 204) {  // No content
                if(success_callback) {
                    success_callback()
                }
                return
            }
>>>>>>> c418497 (2-7답변등록까지 커밋)
            response.json()
                .then(json => {
                    if(response.status >= 200 && response.status < 300) {  // 200 ~ 299
                        if(success_callback) {
                            success_callback(json)
                        }
                    }else {
                        if (failure_callback) {
                            failure_callback(json)
                        }else {
                            alert(JSON.stringify(json))
                        }
                    }
                })
                .catch(error => {
                    alert(JSON.stringify(error))
                })
        })
}

export default fastapi