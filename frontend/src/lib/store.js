import { writable } from 'svelte/store'

// 지속성 스토어 변수 생성 함수
// localStorage에 해당하는 key 가 있으면 기존의 값 사용
// 없으면 초기값으로 생성
const persist_storage = (key, initValue) => {
    const storedValueStr = localStorage.getItem(key)
    // localStorage에 저장되는 값들은 항상 문자열
    // 저장할땐 JSON.stringify , 읽을 때는 JSON.parse 사용
    const store = writable(storedValueStr != null ? JSON.parse(storedValueStr) : initValue)
    // store가 바뀔 때 마다 success_callback함수 사용
    store.subscribe((val) => {
        localStorage.setItem(key, JSON.stringify(val))
    })
    return store
}

// 변수명 : page 초기값 : 0으로 설정
export const page = persist_storage("page", 0)