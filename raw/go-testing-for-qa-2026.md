# Go Testing for QA Engineers

**Дата:** 2026-06-28
**Контекст:** Подготовка к Avito Test Lead — Go как ожидаемый язык

---

## Зачем QA знать Go

Avito использует Go как один из основных языков back-end разработки. Test Lead должен:
- Понимать, как тестируется Go-код
- Писать тесты на Go для API/интеграций
- Оценивать качество Go unit-тестов разработчиков
- Участвовать в code review Go-тестов

---

## Основы Go Testing

### `testing` package

```go
import "testing"

func TestAdd(t *testing.T) {
    got := Add(2, 3)
    want := 5
    if got != want {
        t.Errorf("Add(2, 3) = %d; want %d", got, want)
    }
}
```

**Запуск:** `go test ./...` — рекурсивно все тесты в пакетах.

### Table-Driven Tests (стандарт Go)

```go
func TestAdd(t *testing.T) {
    tests := []struct {
        name string
        a, b int
        want int
    }{
        {"positive", 2, 3, 5},
        {"negative", -1, -2, -3},
        {"zero", 0, 0, 0},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := Add(tt.a, tt.b)
            if got != tt.want {
                t.Errorf("Add(%d, %d) = %d; want %d", tt.a, tt.b, got, tt.want)
            }
        })
    }
}
```

**Почему это важно:** Table-driven tests — идиоматический Go. Разработчики Avito пишут именно так. Test Lead должен понимать и ревьюить этот формат.

### Subtests (`t.Run`)

Позволяют:
- Запускать отдельные кейсы: `go test -run TestAdd/positive`
- Параллельное выполнение: `t.Parallel()` внутри subtests
- Чистый вывод: каждый subtest — отдельная строка в отчёте

---

## `httptest` — тестирование HTTP сервисов

```go
func TestHandler(t *testing.T) {
    handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(http.StatusOK)
        w.Write([]byte(`{"status":"ok"}`))
    })
    
    server := httptest.NewServer(handler)
    defer server.Close()
    
    resp, err := http.Get(server.URL + "/api/health")
    // assert...
}
```

**Для QA:** httptest позволяет тестировать API без поднятия реального сервера. Используется для контрактных тестов и интеграционных проверок.

---

## `testify` — assertion library

Самый популярный Go testing framework:

```go
import "github.com/stretchr/testify/assert"

func TestSomething(t *testing.T) {
    assert.Equal(t, 123, result, "they should be equal")
    assert.NotNil(t, result)
    assert.True(t, result.IsValid())
    assert.Contains(t, response.Body, "expected text")
}
```

**`testify/suite`** — группировка тестов по классам (как describe в Jest):

```go
type ProductTestSuite struct {
    suite.Suite
    db *sql.DB
}

func (s *ProductTestSuite) SetupTest() {
    s.db = setupTestDB()
}

func (s *ProductTestSuite) TestCreateProduct() {
    // используем s.db
    s.Assert().NotNil(result)
}
```

---

## Contract Testing (pact-go)

```go
import "github.com/pact-foundation/pact-go/v2/consumer"

func TestConsumerContract(t *testing.T) {
    pact := consumer.NewConsumerPact(...)
    pact.AddInteraction().
        UponReceiving("a request for product").
        WithRequest(http.MethodGet, "/products/1").
        WillRespondWith(http.StatusOK, ...)
    
    // Run consumer test against pact mock
    // Verify provider later
}
```

**Для Avito:** Контрактные тесты критичны для интеграции команды 1 (агрегатор) → команда 2. Pact-go — стандартный подход.

---

## Coverage

```bash
go test -coverprofile=coverage.out ./...
go tool cover -html=coverage.out  # визуализация
```

Test Lead контролирует: coverage > 50-80% (согласно соседскому соглашению Avito).

---

## Go Testing Best Practices (Avito-style)

| Практика | Описание |
|----------|----------|
| **Table-driven tests** | Стандартный паттерн для всех unit-тестов |
| **Test package** | `package foo_test` — тесты в отдельном пакете |
| **No globals** | Состояние тестов изолировано |
| **Subtests** | `t.Run` для структурирования |
| **Parallel** | `t.Parallel()` для ускорения CI |
| **httptest** | Для API-тестов без реального сервера |
| **testify** | Ассерты для читаемости |
| **Golden files** | `testdata/*.golden` для сложных output |
| **Fuzzing** | `testing/f` для property-based тестов (Go 1.18+) |

---

## План изучения (4 часа)

| Этап | Тема | Время | Результат |
|------|------|-------|-----------|
| 1 | `testing` + table-driven | 1ч | Написать 3 table-driven теста |
| 2 | `httptest` | 1ч | Протестировать HTTP handler |
| 3 | `testify` | 1ч | Переписать тесты с testify |
| 4 | Contract testing | 1ч | Понимание pact-go концепции |

---

## Резюме для интервью

> «Go — мой дополнительный язык. Написал 9 API тестов на Go для Antigravity: table-driven tests с SQL injection, boundary validation, httptest для mock. Понимаю Go testing идиомы: `testing` package, table-driven, testify. Готов перейти на Go как основной — уже делал переезд C# → TS → Python.»

---

## Источники

- [Go testing package](https://pkg.go.dev/testing)
- [Go blog: Table-driven tests](https://go.dev/blog/subtests)
- [Avito Tech — Perforator](https://github.com/avito-tech/perforator) (Go open source)
- [The Art of Go Testing](https://go.dev/wiki/TableDrivenTests)
