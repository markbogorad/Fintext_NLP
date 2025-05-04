# `#OOTT`: Real-Time Sentiment-Based Trading Strategy

This final experiment aims to integrate previously developed techniques into a real-world financial context — specifically, oil trading. The strategy centers on real-time sentiment classification of tweets containing the `#OOTT` (Organization of Oil Traders on Twitter) hashtag, a well-followed tag among energy market participants.

Using Natural Language Processing (NLP), tweets are classified into **positive**, **neutral**, or **negative** sentiment categories. Based on this classification, a simple sentiment-driven trading signal is constructed:

* A **+1 long position** is triggered when the average sentiment over a given window exceeds a positive threshold.
* A **-1 short position** is triggered when the average sentiment falls below a negative threshold.

This approach tests the feasibility of applying real-time NLP classification to market-relevant social media data, offering a proof of concept for sentiment-based trading signals in the energy sector.