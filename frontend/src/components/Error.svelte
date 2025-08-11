<script>
    export let error  // 전달받은 오류
</script>

<!--일반 오류 처리-->
{#if typeof error.detail === 'string'}
    <ul>
        <li>{error.detail}</li>
    </ul>
<!--필드 오류 처리-->
{:else if typeof error.detail === 'object' && error.detail.length > 0 }
    <ul>
        {#each error.detail as err, i}
        <li>
            <strong>{err.loc[1]}</strong> : {err.msg}
        </li>
        {/each}
    </ul>
{/if}