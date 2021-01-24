import os
os.system("export DISPLAY=:0.0")

#######################################################
####       Train with YouTubeCrash dataset       ######
#######################################################

seed = 0
ttc = 1.8
feature_extractor = 'vgg16'
optimizer = 'adam'
lr = 0.0001
decay_lr_per = 3

for n_RGBs, n_BBs in [(3,3)]:

	os.system("python train.py " + \
				"--name youtubeCrash.t-{ttc}s/".format(ttc=ttc) +\
						"{n_RGBs}rgb{n_BBs}b.{feature_extractor}.{optimizer}.lr{lr}.decay_lr_per{decay_lr_per}.seed{seed} ".format(
								n_RGBs=n_RGBs, n_BBs=n_BBs, feature_extractor=feature_extractor,
								optimizer=optimizer, lr=lr, decay_lr_per=decay_lr_per, seed=seed)+ \
				"--train_root ./datasets/YouTubeCrash/train/ "+ \
				"--valid_root ./datasets/YouTubeCrash/test/ "+ \
				"--test_root ./datasets/YouTubeCrash/test/ "+ \
				"--ttc_threshold {} ".format(ttc)+ \
				"--n_rgbs_per_sample {} ".format(n_RGBs)+ \
				"--n_bbs_per_sample {} ".format(n_BBs)+ \
				"--feature_extractor {} ".format(feature_extractor)+ \
				"--optimizer {} ".format(optimizer)+ \
				"--lr {} ".format(lr)+ \
				"--decay_lr_per {} ".format(decay_lr_per)+ \
				"--batch_norm "+ \
				"--nepoch 10 "+ \
				"--eval_freq 45 "+ \
				"--init_steps_to_skip_eval 4000 "+ \
				"--n_train_samples_to_eval 256 "+ \
				"--n_valid_samples_to_eval 0 "+ \
				"--seed {} ".format(seed)
		)

