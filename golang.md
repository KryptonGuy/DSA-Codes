

### Set:

* Description: Collection of distinct elements
* Operations: Insertion (if not present), Deletion, Membership testing
* Go Implementation: set := make(map[ElementType]struct{})
* Examples: Students in a class, Countries in the world

``` go
    // Time: O(n)
    // Space: O(n)
    func containsDuplicate(nums []int) bool {
        // Space: O(n)
        set := NewSet()
        
        // Time: O(n)
        for _, num := range nums {
            // Time: O(1)
            if set.Has(num) {
                return true
            }
            // Time: O(1)
            set.Add(num)
        }

        return false
    }

    type Set struct {
        items map[int]struct{}
    }

    func NewSet() *Set{
        return &Set{
            items: make(map[int]struct{}),
        }
    }

    // Time: O(1)
    // Space: O(1)
    func (s *Set) Add(val int) {
        // Time: O(1)
        s.items[val] = struct{}{}
    }

    // Time: O(1)
    // Space: O(1)
    func (s *Set) Has(val int) bool {
        // Time: O(1)
        _, ok := s.items[val]
        return ok
    } 

```

### Multiset (Bag)

* Description: Collection where elements can appear multiple times
* Operations: Insertion (anytime), Deletion (specific occurrence), Counting occurrences
* Go Implementation: multiset := make(map[ElementType]int) where int is the occurence
* Examples: Word frequency in a document, Fruit counts in a basket

``` go

func containsDuplicate(nums []int) bool {
    set := make(map[int]struct{})
    for _, num := range nums {
        if _, hasNum := set[num]; hasNum {
            return true
        }
        set[num] = struct{}{}
    }
    return false
}

```


### Sorting of String

``` go

func sortString(s string) string {
	characters := []rune(s)
	sort.Slice(characters, func(i, j int) bool {
		return characters[i] < characters[j]
	})
	return string(characters)

    ```