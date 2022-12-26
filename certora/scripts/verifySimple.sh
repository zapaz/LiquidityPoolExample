certoraRun contracts/Pool.sol contracts/Asset.sol  \
    --verify Pool:certora/specs/simple.spec \
    --msg "Pool with no summarization" \
    --link   Pool:asset=Asset \
    --send_only
