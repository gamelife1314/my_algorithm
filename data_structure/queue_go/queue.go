package queue_go

type EmptyQueueException struct{}

func (ex EmptyQueueException) Error() string {
	return "empty queue"
}

type Queue struct {
	data     []int
	capacity int
	head     int
	tail     int
}

func NewQueue(capacity int) *Queue {
	return &Queue{
		data:     make([]int, capacity),
		capacity: capacity,
		head:     0,
		tail:     0,
	}
}

func (q *Queue) Enqueue(value int) bool {
	if q.tail == q.capacity {
		if q.head == 0 {
			return false
		}
		for i := q.head; i < q.tail; i++ {
			q.data[i-q.head] = q.data[i]
		}
		q.tail -= q.head
		q.head = 0
	}
	q.data[q.tail] = value
	q.tail += 1
	return true
}

func (q *Queue) Dequeue() int {
	if q.head == q.tail {
		panic(EmptyQueueException{})
	}
	ret := q.data[q.head]
	q.head += 1
	return ret
}

func (q *Queue) Length() int {
	return q.tail - q.head
}
