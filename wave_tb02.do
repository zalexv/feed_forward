onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate -color Coral -itemcolor Coral /tb/modem_rx_top_inst/sync_find
add wave -noupdate -color Coral -itemcolor Coral -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/loss_cnt
add wave -noupdate /tb/pilot_ce_test
add wave -noupdate /tb/pilot_ce_test_1w
add wave -noupdate /tb/test_tx_inst/pilot_ce
add wave -noupdate /tb/modem_rx_top_inst/clk
add wave -noupdate /tb/modem_rx_top_inst/freq_ce
add wave -noupdate /tb/pilot_start
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/freq_value
add wave -noupdate /tb/modem_rx_top_inst/s_pilot_start_norm
add wave -noupdate /tb/modem_rx_top_inst/s_pilot_start
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/freq_val_filt_mult_1w
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/dds_cos
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/dds_sin
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/time_for_freqcalc_ce
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/time_for_freqcalc_cnt
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/time_for_freqcalc_cnt_reg
add wave -noupdate -divider {New Divider}
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/clk
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/reset
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/sample_ce
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/corri_o
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/corrq_o
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/samplei
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/sampleq
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/pilot_start
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/correlation_sqrt2
add wave -noupdate -format Analog-Step -height 50 -max 16000.0 -radix unsigned /tb/modem_rx_top_inst/pilot_finder_inst/correlation_sqrt
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/correlation_sqrt_p2
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/correlation_sqrt_p1
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/correlation_sqrt_w1
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/correlation_sqrt_max
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/samplei_sq
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/sampleq_sq
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/sample_sq
add wave -noupdate -format Analog-Step -height 70 -max 16000.0 -radix unsigned /tb/modem_rx_top_inst/pilot_finder_inst/cor_test
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/cor_filtered
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/samplei_corr
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/sampleq_corr
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/cor_filtered_ce
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/cor_sqrt_ce
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/sample_ce_w1
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/cor_filtered_mult
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/more_than_porog
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/time_out
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/time_out1
add wave -noupdate /tb/modem_rx_top_inst/pilot_finder_inst/extremum_stm
add wave -noupdate -divider {New Divider}
add wave -noupdate /tb/modem_rx_top_inst/delayer_de/p_rd
add wave -noupdate /tb/modem_rx_top_inst/s_pilot_start
add wave -noupdate /tb/modem_rx_top_inst/start_delayer_cnt
add wave -noupdate /tb/modem_rx_top_inst/start_pilotu
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/delayer_de/p_wr
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/clk
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/reset
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/ce
add wave -noupdate -format Analog-Step -height 80 -max 9000.0 -min -9000.0 -radix decimal /tb/modem_rx_top_inst/scalar_mult_inst/ai
add wave -noupdate -format Analog-Step -height 80 -max 9000.0 -min -9000.0 -radix decimal /tb/modem_rx_top_inst/scalar_mult_inst/aq
add wave -noupdate -format Analog-Step -height 40 -max 9000.0 -min -9000.0 -radix decimal -subitemconfig {/tb/modem_rx_top_inst/scalar_mult_inst/bi(15) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(14) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(13) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(12) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(11) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(10) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(9) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(8) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(7) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(6) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(5) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(4) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(3) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(2) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(1) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/bi(0) {-radix unsigned}} /tb/modem_rx_top_inst/scalar_mult_inst/bi
add wave -noupdate -format Analog-Step -height 40 -max 9000.0 -min -9000.0 -radix decimal /tb/modem_rx_top_inst/scalar_mult_inst/bq
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/sum_ce
add wave -noupdate -radix unsigned -subitemconfig {/tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(31) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(30) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(29) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(28) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(27) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(26) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(25) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(24) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(23) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(22) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(21) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(20) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(19) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(18) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(17) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(16) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(15) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(14) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(13) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(12) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(11) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(10) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(9) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(8) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(7) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(6) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(5) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(4) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(3) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(2) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(1) {-radix unsigned} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o(0) {-radix unsigned}} /tb/modem_rx_top_inst/scalar_mult_inst/sumi_o
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/sumq_o
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/sum_regi
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/sum_regq
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/mul_regi
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/mul_regq
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/aibi
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/aqbq
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/aibq
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/aqbi
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/aibi_m_aqbq
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/aibq_p_aqbi
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/aibi_p_aqbq
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/aqbi_m_aibq
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/ce_w1
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/ce_w2
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/ce_w3
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/scalar_mult_inst/ce_w4
add wave -noupdate -divider {New Divider}
add wave -noupdate /tb/modem_rx_top_inst/pilot_upper_inst/clk
add wave -noupdate /tb/modem_rx_top_inst/pilot_upper_inst/reset
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/pilot_upper_inst/pilot_valid
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/pilot_upper_inst/samplei_o
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/pilot_upper_inst/sampleq_o
add wave -noupdate /tb/modem_rx_top_inst/pilot_upper_inst/test_val
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/pilot_upper_inst/o_interp_ce
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/pilot_upper_inst/o_interp_ce_w1
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/pilot_upper_inst/o_interp_ce_w2
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/pilot_upper_inst/sm_qam_ce
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/cnt_interp
add wave -noupdate -radix unsigned -subitemconfig {/tb/modem_rx_top_inst/pilot_upper_inst/cnt(5) {-height 15 -radix unsigned} /tb/modem_rx_top_inst/pilot_upper_inst/cnt(4) {-height 15 -radix unsigned} /tb/modem_rx_top_inst/pilot_upper_inst/cnt(3) {-height 15 -radix unsigned} /tb/modem_rx_top_inst/pilot_upper_inst/cnt(2) {-height 15 -radix unsigned} /tb/modem_rx_top_inst/pilot_upper_inst/cnt(1) {-height 15 -radix unsigned} /tb/modem_rx_top_inst/pilot_upper_inst/cnt(0) {-height 15 -radix unsigned}} -expand -subitemconfig {/tb/modem_rx_top_inst/pilot_upper_inst/cnt(5) {-height 15 -radix unsigned} /tb/modem_rx_top_inst/pilot_upper_inst/cnt(4) {-height 15 -radix unsigned} /tb/modem_rx_top_inst/pilot_upper_inst/cnt(3) {-height 15 -radix unsigned} /tb/modem_rx_top_inst/pilot_upper_inst/cnt(2) {-height 15 -radix unsigned} /tb/modem_rx_top_inst/pilot_upper_inst/cnt(1) {-height 15 -radix unsigned} /tb/modem_rx_top_inst/pilot_upper_inst/cnt(0) {-height 15 -radix unsigned}} /tb/modem_rx_top_inst/pilot_upper_inst/cnt
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/pilot_upper_inst/mod_samplesi
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/pilot_upper_inst/mod_samplesq
add wave -noupdate -radix binary /tb/modem_rx_top_inst/pilot_upper_inst/bits
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/pilot_upper_inst/s_samplei_o
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/pilot_upper_inst/s_sampleq_o
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/cnt_delay
add wave -noupdate -radix decimal /tb/modem_rx_top_inst/pilot_upper_inst/cnt_pilot
add wave -noupdate /tb/modem_rx_top_inst/pilot_upper_inst/qam4_mapper_inst/clk
add wave -noupdate /tb/modem_rx_top_inst/pilot_upper_inst/qam4_mapper_inst/reset
add wave -noupdate /tb/modem_rx_top_inst/pilot_upper_inst/qam4_mapper_inst/i_bits
add wave -noupdate /tb/modem_rx_top_inst/pilot_upper_inst/qam4_mapper_inst/i_ce
add wave -noupdate /tb/modem_rx_top_inst/pilot_upper_inst/qam4_mapper_inst/o_samplesi
add wave -noupdate /tb/modem_rx_top_inst/pilot_upper_inst/qam4_mapper_inst/o_samplesq
add wave -noupdate /tb/modem_rx_top_inst/pilot_upper_inst/qam4_mapper_inst/o_ce
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/clk
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/reset
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/i_samplesi
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/i_samplesq
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/o_samplei
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/o_sampleq
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/muls_i
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/muls_q
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/delaylinei
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/delaylineq
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/sumsi_1
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/sumsq_1
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/sumsi_2
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/sumsq_2
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/sumsi_3
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/sumsq_3
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/sumsi_4
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/sumsq_4
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/sumsi_5
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/sumsq_5
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/s_o_samplei
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilot_upper_inst/rcc_up_filter_inst/s_o_sampleq
add wave -noupdate -divider {New Divider}
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/clk
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/reset
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/realpilot_event
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/start_pilotu
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/sync_find
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/start_pilotu_have
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/s_start_pilotu
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/start_delayer_cnt
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/loss_cnt
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/stm
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/main_cnt_prev_a
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/main_cnt_best
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/main_cnt_prev
add wave -noupdate -radix unsigned -subitemconfig {/tb/modem_rx_top_inst/pilotsync_inst/main_cnt(13) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(12) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(11) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(10) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(9) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(8) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(7) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(6) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(5) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(4) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(3) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(2) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(1) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(0) {-radix unsigned}} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt
add wave -noupdate -radix unsigned -subitemconfig {/tb/modem_rx_top_inst/pilotsync_inst/main_cnt(13) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(12) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(11) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(10) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(9) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(8) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(7) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(6) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(5) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(4) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(3) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(2) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(1) {-radix unsigned} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt(0) {-radix unsigned}} /tb/modem_rx_top_inst/pilotsync_inst/main_cnt
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/main_cnt_prev_sum
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/s_sync_find
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/one_p
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/g_start_pilotu_have
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/g_start_pilotu
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/g_start_delayer_cnt
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/m_start_pilotu_have
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/m_start_pilotu
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/m_start_delayer_cnt
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/m_realpilot_event
add wave -noupdate -radix unsigned /tb/modem_rx_top_inst/pilotsync_inst/good_come
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {1780022968 ps} 0}
configure wave -namecolwidth 377
configure wave -valuecolwidth 87
configure wave -justifyvalue left
configure wave -signalnamewidth 0
configure wave -snapdistance 10
configure wave -datasetprefix 0
configure wave -rowmargin 4
configure wave -childrowmargin 2
configure wave -gridoffset 0
configure wave -gridperiod 1
configure wave -griddelta 40
configure wave -timeline 0
configure wave -timelineunits ps
update
WaveRestoreZoom {0 ps} {2388393 ns}
