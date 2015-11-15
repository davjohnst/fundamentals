#!/usr/bin/env python

class TextJustification(object):

    """
    This is how LateX justifies its text

    Goal: split text into "good" lines
       where the text is an array of words, size N

    Def badness(i,j) = how "bad" it would be to use words i, ..., j-1 as a line

             INF if the text doesn't fit on the line
         = /
           \ (page width - words width) ^3

    New goal: minimize the total badness of all lines

    Define subproblem:
       total badness of words[i:N-1]
       number of subproblems: N

    What to guess in each subproblem?
       where to break the next line

    Define recurrence:
       total_badness(words[i:N]) = min_j {   badness[i,j] + total_badness(words[j:N])  }

    What's the overall solution?
       total_badness(words[0:N])
       keeping parent pointers will give us the line breaks that minimizes cost

    """

    def __init__(self, page_width):
        self.page_width = page_width


    def justify(self, words):

        max_length = max([len(w) for w in words])
        if max_length > self.page_width:
            raise ValueError("can't fit at least one word into the page width")

        N = len(words)
        total_badness = [None] * (N + 1)
        total_badness[N] = (0, None)

        # call into recursive justify
        ans = self._justify_rec(words, total_badness, 0, N)

        uniq_breaks = []
        current = None
        for x in total_badness:
            if x[1] != current and x[1] is not None:
                uniq_breaks.append(x[1])
                current = x[1]

        results = []
        last = None
        for i in uniq_breaks:
            if last is None:
                last = 0
            results.append(" ".join(words[last:i]))
            last = i

        return "\n".join(results)




    def _justify_rec(self, words, total_badness, i, N):
        """
        Solves the recursive step: what is the optimal line breaking with words[i:] ?

        :param words: Word list with words from 0..N-1
        :param total_badness: Dynamic solution array
        :param i: Defines "subproblem" of finding best solution of words[i:]
        :return: nothing! we'll fill in the DP array
        """

        if total_badness[i]:
            return total_badness[i][0]

        min_cost = float("inf")
        min_parent = None

        # compute min_j badness(i,j) + total_badness[j]
        for j in range(i+1, N+1):
            current_cost = self.line_badness(words[i:j]) + self._justify_rec(words, total_badness, j, N)
            if current_cost < min_cost:
                min_cost = current_cost
                min_parent = j

        total_badness[i] = (min_cost, min_parent)
        return min_cost

    def line_badness(self, line):
        length = len(" ".join(line))
        if length > self.page_width:
            return float("inf")
        else:
            return abs((self.page_width - length)**3)


def main():
    tj = TextJustification(10)
    print tj.justify(["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"])


if __name__ == "__main__":
    main()