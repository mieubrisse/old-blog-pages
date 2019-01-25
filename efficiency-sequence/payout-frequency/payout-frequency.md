Payout Frequency
================
In [Exponentiation Tradeoffs](../exponentiation-tradeoffs.md) I introduced an equation for estimating the yield from an exponential trade, `net_payout = (magnitude_of_payout x number_of_payouts) - initial_investment`, and applied it to our example of training your dog to fetch your newspaper. In the example, we estimated the `number_of_payouts` would be 7 years of newspaper-fetching (if training began at age 1) x 365 days in a year x some reduction multiplier to account for uncertainty (because maybe the newspaper doesn't arrive some days or your dog is lazy or prone to sickness). Seems straightforward, but notice: the frequency of the payout is high (daily), so a fetching failure of any single day isn't a big deal - you only lose out on 4 minutes of potential time saved. What happens when the payout frequency is lower?

Imagine that you've retired and, in pursuit of some peace and relaxation, have moved from suburbia out to the country. Finally free from your neighbor Beth and her noisy children, you've purchased a 30-acre plot of land located a 2.5 hour's drive from the nearest city. Rural life is slower though - the town news is published only once a week, and the postman leaves newspapers for far-flung subscribers like yourself at the town's post office. Your previous dog went to doggy heaven just before you left the suburban life behind, but so impressed were you with its newspaper-fetching that you've purchased a golden retriever puppy for your new home  - an enthusiastic little hound, eager to learn and please. Your puppy has just turned 1 and you're keen to start his training (fondly envisioning the little newspaper wagon you'll get him to tug to town and back), so let's put some numbers to your scenario and calculate your savings:

* Each round trip to town takes a little under 5 hours (292 minutes, or 4.86 hours, to be precise)
* Newspapers are retrieved 5 times per year
* For the sake of example, we'll assume your puppy still takes a year to train
* Using the same golden retriever average lifespan from before, your puppy will have 7 newspaper-fetching years

Plugging these figures into our equation, we see that the total payout = 292 minutes (magnitude of payout) x 5 payouts per year x 7 years = 10,220 minutes, roughly 7 days, saved over your new dog's lifespan. This just so happens (by coincidence, of course) to be the exact same return yielded by your previous dog in your suburban home. But wait - these situations are _not_ identical! Because the magnitude of each rural payout is much higher (292 minutes for your new house vs. 4 minutes in your suburban home), each individual payout in the country comprises a greater share of the total payout. If something goes wrong with a single trip to town in your new house, your net payout has decreased by nearly 5 hours!

To see this in action, let's gather some data. I've written [a small computer program](payout-frequency-example.py) that simulates all fetches over the life of your dog (using a given probability of failure for each fetch) and prints the number of successful fetches as well as the total time you saved by training your dog - the gross payout. The program will repeat this process multiple times to simulate your dog's lifespan in multiple alternate realities, so we can see several possible alternatives for what his life could look like (with the assumption that he doesn't die prematurely).

I'll set my program inputs using the numbers above, so `num_fetches_in_dog_lifetime` = 35 (7 years x 5 fetches per year) and `minutes_saved_per_successful_fetch` = 292 (4.86 hours). I'll arbitrarily choose `probability_of_successful_fetch` = 0.9, and we want lots of data so I'll use `num_alternate_realities` = 10,000. Here are the first 10 rows of generated data corresponding to 10 alternate realities:

| Number of Successful Fetches | Total Minutes Saved |
| ---------------------------- | ------------------- |
| 31                           | 9052                |
| 33                           | 9636                |
| 31                           | 9052                |
| 31                           | 9052                |
| 26                           | 7592                |
| 31                           | 9052                |
| 33                           | 9636                |
| 30                           | 8760                |
| 32                           | 9344                |
| 30                           | 8760                |

_[Click here to download all 10,000 rows as CSV](fetch-5-times-per-year.csv)_

Calculating the mean, minimum, maximum, and standard deviation of the minutes saved yields:

```
Mean: 9194.17 minutes saved (6.38 days)
Minimum: 7008 (4.9 days)
Maximum: 10220 (7.1 days)
Standard Deviation: 521.24 (0.36 days)
```

For comparison, I'll also calculate the number of successful fetches and time saved for your dog in your suburban home over multiple alternate realities. The only variables we'll change are the number of fetches and the minutes saved per fetch, setting `num_fetches_in_dog_lifetime` = 2555 (7 years x 365 fetches per year) and `minutes_saved_per_successful_fetch` = 4. With `probability_of_successful_fetch` and `num_alternate_realities` untouched at 0.9 and 10,000 respectively, here's our output: 

| Number of Successful Fetches | Total Minutes Saved |
| ---------------------------- | ------------------- |
| 2285                         | 9140                |
| 2302                         | 9208                |
| 2324                         | 9296                |
| 2280                         | 9120                |
| 2299                         | 9196                |
| 2315                         | 9260                |
| 2273                         | 9092                |
| 2293                         | 9172                |
| 2289                         | 9156                |
| 2282                         | 9128                |

_[Click here to download all 10,000 rows as CSV](fetch-every-day.csv)_

Calculating the same characteristics on this dataset:

```
Mean: 9198.18 minutes saved (6.39 days)
Minimum: 8972 (6.2 days)
Maximum: 9432 (6.6 days)
Standard Deviation: 60.17 (0.042 days)
```

The means of both datasets are very similar (no surprise; both cases have the same expected value of 90% probability of success x 1460 minutes saved per year x 7 years of life = an average 9198 minutes, or 6.4 days, saved over the dog's lifespan), yet the spread of minutes saved across alternate realities is much wider when fetching the newspaper in the country than in suburbia. In one reality you only save 7008 minutes = 4.86 days, a full 1.5 days less than the expected value, while in another you save 10220 minutes = 7.1 days! This wide range is easily seen when comparing the datasets' standard deviations: the country dataset's standard deviation is nearly 10 times that of the suburban case.

As we discussed earlier, the explanation for this behaviour lies in the high magnitude and low frequency of payouts in the country scenario. Because your dog is saving _so_ much time with every trip it makes to town, each failed trip means a significant reduction in the total return on your exponential trade. Though the scenarios are equivalent in their expected minutes saved, expected value is not the only characteristic we must evaluate when considering an exponential trade! Of course, investors and grandmothers alike have passed down this wisdom for centuries as "don't put all your eggs in one basket" - if a basket breaks then omelette famine reigns. Two exponential trades with equivalent `total_payout` values but vastly different `number_of_payouts` (and therefore, `magnitude_of_payouts`) are _not_ equivalent; be wary of low-frequency payouts!
