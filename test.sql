SELECT
  DENSE_RANK() OVER (
    ORDER BY
      v
  ) my_dense_rank,
  RANK() OVER (
    ORDER BY
      v
  ) my_rank
