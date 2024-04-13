from attacks import interweaveTexts

#prompt
input_text = "The following sentences are taken from the abstract of a scientific paper. Artificial Intelligence (AI) has received an increasing amount of attention in multiple areas."

#llm output without watermark
decoded_output_without_watermark = "The following sentences are taken from the abstract of a scientific paper. Artificial Intelligence (AI) has received an increasing amount of attention in multiple areas. In the field of Artificial Intelligence, many areas of theoretical and statistical analysis and AI have been published. The main focus of the present paper is the development of an AI system capable of performing complex tasks..."

#llm output with watermark
decoded_output_with_watermark = "The following sentences are taken from the abstract of a scientific paper. Artificial Intelligence (AI) has received an increasing amount of attention in multiple areas. The rise in the popularity of the artificial intelligence, artificial intelligence, and robotics has largely been due to a combination of the two. These two developments make possible the creation of new technologies, artificial intelligence, and robotics. The following sentence can be interpreted as an analogy; they both imply that AI can be found on a much lower level of the level of the human intellect."

#human response
human_response = "The following sentences are taken from the abstract of a scientific paper. Artificial Intelligence (AI) has received an increasing amount of attention in multiple areas.The uncertainties and risks in AI-powered systems have created reluctance in their wild adoption. As an economic solution to compensate for potential damages, AI liability insurance is a promising market to enhance the integration of AI into daily life. In this work, we use an AI-powered E-diagnosis system as an example to study AI liability insurance."

print(interweaveTexts(decoded_output_with_watermark, human_response, 0.5))