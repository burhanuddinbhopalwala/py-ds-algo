SELECT
  DENSE_RANK() OVER (
    PARTITION BY c1
    ORDER BY
      c2
  ) AS my_dense_rank,
  RANK() OVER (
    PARTITION BY c1
    ORDER BY
      c2
  ) AS my_rank
FROM
  tests;
