const llenarArray = () => {
  const array = []
  for (let i = 0; i <= 49; i++) {
    array.push(Math.random())
  }
  return array
}

const ordenarArray = (array) => {
  const n = array.length
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - 1; j++) {
      if (array[j] > array[j + 1]) {
        ;[array[j], array[j + 1]] = [array[j + 1], array[j]]
      }
    }
  }
  return array
}

array = llenarArray()

/* Mostrar array original */
console.log(array)

/* Mostrar array ordenado */
console.log(ordenarArray(array))
