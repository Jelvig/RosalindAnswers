"""Mendels First-Law Given how many organims have dominant, heterozygous, and recessive.
The probability that two randomly selected mating organisms will produce an individual possessing a
 dominant allele. Assume that any two organisms can mate."""


def probability(homo_dominant:int, heter:int, homo_rec:int) -> float:
	total = homo_dominant + heter + homo_rec

	dominantTotal = homo_dominant/total
	heterozygousDom_Total = (heter/total) * ((homo_dominant/(total-1)) + (heter-1)/(total-1) * 0.75 + ((homo_rec/(total-1)) * 0.5))
	domHeterRecesTotal = (homo_rec/total) * (homo_dominant/(total-1) + heter/(total-1) * 0.5)


	Homo_total = dominantTotal + heterozygousDom_Total + domHeterRecesTotal
	return Homo_total

if __name__ == "__main__":

	result = round(probability(17.0, 27.0, 24.0), 5)
	print(result)
