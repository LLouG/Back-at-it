<script>
  let count = $state(0);

  const increment = () => {
    count += 1;
  };

  const reset = () => {
    count = 0;
  };
</script>

<button onclick={increment}>count is {count}</button>

<button onclick={reset}>RESET</button>

<style>
</style>
