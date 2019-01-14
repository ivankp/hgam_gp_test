#ifndef LIN_ALG_HH
#define LIN_ALG_HH

namespace linalg {

template <typename T>
constexpr auto sq(T x) noexcept { return x*x; }
template <typename T, typename... TT>
constexpr auto sq(T x, TT... xx) noexcept { return sq(x)+sq(xx...); }

constexpr unsigned utn(unsigned n) noexcept { return n*(n+1) >> 1; }

void cholesky(double* A, unsigned N) noexcept;
void solve_triang(const double* L, double* v, unsigned n) noexcept;
double dot(const double* a, const double* b, unsigned n) noexcept;

}

#endif
